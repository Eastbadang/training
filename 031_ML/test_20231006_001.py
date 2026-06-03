import numpy as np
import gym

# LTspice 공진 회로 환경 설정
class LCResonanceEnv(gym.Env):
    def __init__(self):
        super().__init__()
        self.L = 6.3e-6  # 고정 인덕턴스 값 (6.3uH)
        self.target_frequency = 100e3  # 목표 주파수 (100kHz)
        self.observation_space = gym.spaces.Box(low=0, high=1000e-9, shape=(1,), dtype=np.float32)  # 캐패시턴스 C 값을 정의합니다.
        self.action_space = gym.spaces.Discrete(101)  # 가능한 행동은 C 값의 0부터 100 사이의 정수입니다.
        self.current_frequency = self.calculate_frequency(0)  # 초기 C 값에 대한 주파수를 계산합니다.

    def calculate_frequency(self, capacitance):
        # 주어진 C 값으로 주파수를 계산합니다. C 값이 0보다 작은 경우 무시합니다.
        capacitance = max(capacitance, 1e-7)  # C 값이 0보다 작지 않도록 최소값을 설정합니다.
        omega = 1 / np.sqrt(self.L * capacitance)
        frequency = omega / (2 * np.pi)
        return frequency

    def step(self, action):
        # 에이전트가 한 단계의 행동을 수행합니다.
        capacitance = action / 100e6  # 0부터 100 사이의 정수를 [0, 1e-6] 범위의 실수로 변환합니다.
        #print(capacitance)
        self.current_frequency = self.calculate_frequency(capacitance)

        # 보상 계산: 목표 주파수와의 차이를 최소화하려고 합니다.
        reward = -abs(self.current_frequency - self.target_frequency)

        # 학습 종료 조건: 목표 주파수와의 차이가 일정 수준 이하인 경우
        done = abs(self.current_frequency - self.target_frequency) < 1e3

        return np.array([capacitance]), reward, done, {}

    def reset(self):
        # 환경을 초기화하고 무작위로 C 값을 선택합니다.
        self.current_frequency = self.calculate_frequency(0)
        return np.array([0.0])

# Q-Learning 알고리즘 구현
class QLearningAgent:
    def __init__(self, env, learning_rate=0.1, discount_factor=0.9, exploration_prob=1.0, exploration_decay=0.995):
        self.env = env
        self.learning_rate = learning_rate
        self.discount_factor = discount_factor
        self.exploration_prob = exploration_prob
        self.exploration_decay = exploration_decay
        self.q_table = np.zeros((1001,))

    def select_action(self, state):
        if np.random.rand() < self.exploration_prob:
            return np.random.randint(self.env.action_space.n)
        else:
            return np.argmax(self.q_table)

    def update_q_table(self, state, action, reward, next_state):
        best_next_action = np.argmax(self.q_table)
        self.q_table[action] += self.learning_rate * (reward + self.discount_factor * self.q_table[best_next_action] - self.q_table[action])
        self.exploration_prob *= self.exploration_decay

# 학습 실행
if __name__ == "__main__":
    env = LCResonanceEnv()
    agent = QLearningAgent(env)

    num_episodes = 10000
    for episode in range(num_episodes):
        state = env.reset()
        done = False
        total_reward = 0

        while not done:
            action = agent.select_action(state)
            # print(action)
            next_state, reward, done, _ = env.step(action)
            agent.update_q_table(state, action, reward, next_state)
            total_reward += reward
            state = next_state

        print(f"Episode {episode + 1}/{num_episodes}, Total Reward: {total_reward}")

    # 학습 완료 후 최적 C 값을 출력
    optimal_c = np.argmax(agent.q_table) / 100e6
    print(f"Optimal Capacitance (C): {optimal_c} F")
