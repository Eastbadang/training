import random
import numpy as np
import time
# from collections import deque

import matplotlib.pyplot as plt
import subprocess as sbp
import csv
import os
import tensorflow as tf
from tensorflow.keras import initializers as init, losses as loss, optimizers as opt
from tensorflow.keras import Model, Input
from tensorflow.keras import metrics
from tensorflow.keras.layers import Dense

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'

# 경로 변수 설정
ansys_location = "C:/Program Files/AnsysEM/AnsysEM21.1/Win64/ansysedt.exe"
maxwell_script_1 = "C:/Users/SPEC_Simul/Desktop/WPT_J2954/1Barrak/WPT_J2954_script_20230109.py"
maxwell_script_2 = "C:/Users/SPEC_Simul/Desktop/WPT_J2954/1Barrak/WPT_J2954_script_20230109_3Deddy.py"


# 네트워크 구축
class NN:
    def __init__(self, input_size_, output_size_):
        self.model = Model()
        self.input_size_ = input_size_
        self.output_size_ = output_size_
        self.l_rate = 0.1
        self.x = np.array([])
        self.y = np.array([])

        self.build_nn()

    def build_nn(self):
        input_ = Input(shape=(self.input_size_,))
        hidden1 = Dense(units=25, activation=tf.nn.relu, use_bias=False, kernel_initializer=init.GlorotUniform())(
            input_)
        hidden1 = Dense(units=25, activation=tf.nn.relu, use_bias=False, kernel_initializer=init.GlorotUniform())(
            hidden1)
        hidden1 = Dense(units=25, activation=tf.nn.relu, use_bias=False, kernel_initializer=init.GlorotUniform())(
            hidden1)
        output_ = Dense(units=self.output_size_, activation='linear', use_bias=True,
                        bias_initializer=init.RandomUniform(minval=0, maxval=0.001))(hidden1)

        self.model = Model(input_, output_)

        self.model.compile(optimizer=opt.Adam(learning_rate=self.l_rate), loss='mean_squared_error', metrics=['mae'])

    def predict(self, input_):
        _input = np.reshape(input_, [1, self.input_size_])
        return self.model.predict(_input, verbose=0, batch_size=1)

    def update(self, _x, _y):
        self.x = np.reshape(_x, [1, self.input_size_])
        self.y = np.reshape(_y, [1, self.output_size_])
        self.model.compile(optimizer=opt.Adam(learning_rate=self.l_rate),
                           loss=loss.MeanSquaredError(), metrics=metrics.MeanAbsoluteError())
        self.model.fit(self.x, self.y, verbose=0)
        return self.model.evaluate(self.x, self.y, verbose=0, batch_size=1)


# Agent
class Agent:
    def __init__(self, nn1):
        self.state, self.next_state, self.greedy_state = reset()
        self.done = False
        self.epsilon = 1
        self.nn1 = nn1
        self.cube_select = 12
        self.exploit_idx = 0
        self.argmax = []

    def set_action(self):
        self.next_state = list(np.zeros(24, dtype=np.int64))
        self.done = False
        self.epsilon = max(1 - (step / num_episodes), 0.1)
        self.exploit_idx = 0
        self.argmax.clear()

        if np.random.rand(1) < self.epsilon:
            print("Exploration")
            choose_explore = list(np.random.choice(24, 12, replace=False))
            choose_explore.sort()
            for choose in choose_explore:
                self.next_state[choose] = 1
        else:
            print("Exploitation")
            for j in range(self.cube_select):
                pred = self.nn1.predict(Action_list[max_reward_idx])[0]
                if j > 0:
                    for idx in self.argmax:
                        pred[idx] = 0
                select = np.argmax(pred)
                self.next_state[select] = 1
                self.argmax.append(select)
                self.state = self.next_state

        self.next_state = list(self.next_state)
        actions.append(list(np.where(np.array(self.next_state) == 1)[0]))

        return self.next_state


def get_top_n(num_array, n):  # 리스트 상위 n개 추출
    num_tmp = num_array[:]
    top_n_num = []
    top_n_idx = []

    num_array.sort()
    for idx in range(n):
        top_n_num.append(num_array[-idx - 1])  # idx = 0부터 시작하므로 -1을 더함
        top_n_idx.append(num_tmp.index(top_n_num[idx]))

    return top_n_idx, top_n_num


def executemaxwell(next_state_):
    cube_count = int(sum(next_state_))
    maxwell_rerun = 0

    ferrite_change_temp = np.where(np.array(next_state_) == 1)[0]
    ferrite_change = []

    for change_index in range(len(ferrite_change_temp)):
        ferrite_change.append(ferrite_change_temp[change_index])

    text = open('Ferrite_choose.py', 'w')

    text.write("Ferrite_change = []")
    text.write("\n")

    for change_index in range(len(ferrite_change)):
        ferrite_change[change_index] = str(ferrite_change[change_index])
        text.write("Ferrite_change.append(" + ferrite_change[change_index] + ")")
        text.write("\n")

    cube_count = str(cube_count)
    text.write("cube_count = " + cube_count)
    text.close()

    ferrite_change.clear()

    maxwell_run_time = time.time()
    sbp.run([ansys_location, "-RunScriptAndExit", maxwell_script_1])

    time.sleep(2)
    while True:
        f = open('M.csv', 'r', encoding='utf-8')
        reader = csv.reader(f)
        lines = list(reader)
        f.close()
        if len(lines[1]) >= 3:
            if (lines[1][1] != '') & (lines[1][2] != ''):
                break
        maxwell_run_time = time.time()
        sbp.run([ansys_location, "-RunScriptAndExit", maxwell_script_2])
        time.sleep(1)
        maxwell_rerun = 2

    result_normal = float(lines[1][1])
    result_misalign = float(lines[1][2])

    return result_normal, result_misalign, maxwell_rerun


def reset():
    state_0 = list(np.zeros(24, dtype=np.int64))
    next_state_0 = list(np.zeros(24, dtype=np.int64))
    greedy_state_0 = list(np.ones(24, dtype=np.int64))

    return state_0, next_state_0, greedy_state_0


# main
input_size, output_size = 24, 24
num_episodes = 300
data_number = int(num_episodes / 10)
max_reward_idx = 0
maxwell_rerun_cnt = 0
maxwell_result_mis = 0

start_time = time.time()

Action_list = []
Result_list = []
Reward_list = []
actions = []
max_M = np.zeros(data_number)

NNet = NN(input_size, output_size)

agent = Agent(NNet)


# ####### 정보 문단 #######
print("J2954_학회버전_24C12_20230109")

print("Reward function: (Mmis/(Mnormal + Mmis) * Mnormal) + (Mnormal/(Mnormal + Mmis) * Mnormal)")

print(num_episodes, "episodes, ", agent.cube_select, "cubes selected, learning rate =", NNet.l_rate)

print("Epsilon: max(1- step/num_episodes, 0.1)")

print("Activation Function: relu, softmax, Initializer: GlorotUniform")

print("Layer Configuration: 24 - 25 - 25 - 25 - 24, 3 hidden layers")

print("etc: None")
# #########################

for step in range(num_episodes):

    maxwell_start_time = time.time()
    print("Episodes: ", step + 1)

    agent.nn1 = NNet
    state = agent.set_action()

    maxwell_result_normal, maxwell_result_mis, maxwell_rerun_flag = executemaxwell(state)
    maxwell_time = time.time() - maxwell_start_time
    time.sleep(1)

    reward_ratio_1 = maxwell_result_normal / (maxwell_result_normal + maxwell_result_mis)
    reward_ratio_2 = maxwell_result_mis / (maxwell_result_normal + maxwell_result_mis)
    reward = maxwell_result_normal * reward_ratio_2 + maxwell_result_mis * reward_ratio_1  # 비율형

    # reward = maxwell_result_normal / (maxwell_result_normal - maxwell_result_mis) # 분수형
    # reward = pow(maxwell_result_normal, maxwell_result_mis) # 지수형 1
    # reward = pow(maxwell_result_normal+maxwell_result_mis, 1/(maxwell_result_normal-maxwell_result_mis)) # 지수형 2

    Action_list += [state]
    Result_list += [[maxwell_result_normal, maxwell_result_mis]]
    Reward_list += [reward]
    maxwell_rerun_cnt += maxwell_rerun_flag

    nn_input = reward * np.array(state, dtype=np.float64)

    cost, mae = NNet.update(nn_input, nn_input)

    print("Action, M:", state, "/ Normal:", maxwell_result_normal, ", misalign:", maxwell_result_mis)
    print("Reward: ", reward)

    max_reward = max(Reward_list)
    for i in range(len(Action_list)):
        if Reward_list[i] == max_reward:
            max_reward_idx = i

    if step // 10 != 0:
        max_M[(step // 10) - 1] = max_reward

    print("Best Action, M:", Action_list[max_reward_idx], "/ Normal:", Result_list[max_reward_idx][0],
          ", misalign:", Result_list[max_reward_idx][1])
    print("Best Reward:", Reward_list[max_reward_idx])
    print("cost: ", cost, "/ Maxwell Rerun: ", maxwell_rerun_cnt)
    print("maxwell time:", maxwell_time, "\n")


fig, ax = plt.subplots()
ax.plot(np.arange(1, len(Reward_list) + 1, 1), Reward_list, 'o-')
ax.set(xlabel='episodes', ylabel='reward')
ax.grid()
plt.show()

nn_output_final = NNet.predict(Action_list[max_reward_idx] * Reward_list[max_reward_idx])[0]

print("final max M at Normal:", Result_list[max_reward_idx][0], "and Misalign:", Result_list[max_reward_idx][1])
print("final cube selection at that k is :", Action_list[max_reward_idx])
print("index of 1 in final cube selection is :", np.where(np.array(Action_list[max_reward_idx]) == 1)[0])

print(nn_output_final)

print("--- %s seconds ---" % (time.time() - start_time))
