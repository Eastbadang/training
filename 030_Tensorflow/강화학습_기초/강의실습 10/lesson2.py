import random
import numpy as np
import matplotlib.pyplot as plt

# 그리드월드 높이와 너비
GRID_HEIGHT = 4
GRID_WIDTH = 12

# 행동의 개수
NUM_ACTIONS = 4

# 초기 상태와 종료 상태
START_STATE = (3, 0)
TERMINAL_STATES = [(3, 11)]
CLIFF_STATES = [
    (3, 1), (3, 2), (3, 3), (3, 4), (3, 5),
    (3, 6), (3, 7), (3, 8), (3, 9), (3, 10)
]


# 스텝 사이즈
ALPHA = 0.5

# 감가율
GAMMA = 1.0

# 최대 에피소드
MAX_EPISODES = 500

# 탐색(exploration) 확률 파라미터
INITIAL_EPSILON = 0.1
FINAL_EPSILON = 0.01
LAST_SCHEDULED_EPISODES = 350

# 총 실험 횟수 (성능에 대한 평균을 구하기 위함)
TOTAL_RUNS = 10

# 비어있는 행동 가치 테이블을 0~1 사이의 임의의 값으로 초기화하며 생성함
def generate_initial_q_value(env):
    q_value = np.zeros((GRID_HEIGHT, GRID_WIDTH, env.NUM_ACTIONS))

    for i in range(GRID_HEIGHT):
        for j in range(GRID_WIDTH):
            if (i, j) not in TERMINAL_STATES:
                for action in env.ACTIONS:
                    q_value[i, j, action] = random.random()
    return q_value

# 모든 상태에서 수행 가능한 행동에 맞춰 임의의 정책을 생성함
# 초기에 각 행동의 선택 확률은 모두 같음
def generate_initial_random_policy(env):
    policy = dict()

    for i in range(GRID_HEIGHT):
        for j in range(GRID_WIDTH):
            if (i, j) not in TERMINAL_STATES:
                actions = []
                action_probs = []
                for action in env.ACTIONS:
                    actions.append(action)
                    action_probs.append(0.25)

                policy[(i, j)] = (actions, action_probs)

    return policy


class CliffGridWorld():
    def __init__(
            self,
            height=4, width=12,         # 격자판의 크기
            start_state=(3, 0),         # 시작 상태
            terminal_states=[(3, 11)],  # 종료 상태
            transition_reward=-1.0,     # 일반적인 상태 전이 보상
            terminal_reward=1.0,        # 종료 상태로 이동하는 행동 수행
                                        # 때 받는 보상
            outward_reward=-1.0,        # 미로 바깥으로 이동하는 행동 수행
                                        # 때 받는 보상 (이동하지 않고 제자리 유지)
            cliff_states_info=None      # 절벽 상태
    ):
        self.__version__ = "0.0.1"

        # 그리드월드의 세로 길이
        self.HEIGHT = height

        # 그리드월드의 가로 길이
        self.WIDTH = width

        self.STATES = []
        self.num_states = self.WIDTH * self.HEIGHT

        for i in range(self.HEIGHT):
            for j in range(self.WIDTH):
                self.STATES.append((i, j))

        for state in terminal_states:     # 터미널 스테이트 제거
            self.STATES.remove(state)

        # 모든 가능한 행동
        self.ACTION_UP = 0
        self.ACTION_DOWN = 1
        self.ACTION_LEFT = 2
        self.ACTION_RIGHT = 3

        self.ACTIONS = [
            self.ACTION_UP,
            self.ACTION_DOWN,
            self.ACTION_LEFT,
            self.ACTION_RIGHT
        ]

        # UP, DOWN, LEFT, RIGHT
        self.ACTION_SYMBOLS = ["↑", "↓", "←", "→"]
        self.NUM_ACTIONS = len(self.ACTIONS)

        # 시작 상태 위치
        self.START_STATE = start_state

        # 종료 상태 위치
        self.TERMINAL_STATES = terminal_states

        # 웜홀 상태 위치
        self.CLIFF_STATES_INFO = cliff_states_info

        # 최대 타임 스텝
        self.max_steps = float('inf')

        self.transition_reward = transition_reward

        self.terminal_reward = terminal_reward
        self.outward_reward = outward_reward

        self.current_state = None

    def reset(self):
        self.current_state = self.START_STATE
        return self.current_state

    def moveto(self, state):
        self.current_state = state

    def is_cliff_state(self, state):
        i, j = state

        if self.CLIFF_STATES_INFO and len(self.CLIFF_STATES_INFO) > 0:
            for cliff_info in self.CLIFF_STATES_INFO:
                cliff_state = cliff_info[0]
                if i == cliff_state[0] and j == cliff_state[1]:
                    return True
        return False

    def get_next_state_cliff(self, state):
        i, j = state
        next_state = None

        for cliff_info in self.CLIFF_STATES_INFO:
            cliff_state = cliff_info[0]
            cliff_prime_state = cliff_info[1]

            if i == cliff_state[0] and j == cliff_state[1]:
                next_state = cliff_prime_state
                break
        return next_state

    def get_reward_cliff(self, state):
        i, j = state
        reward = None

        for cliff_info in self.CLIFF_STATES_INFO:
            cliff_state = cliff_info[0]
            cliff_reward = cliff_info[2]

            if i == cliff_state[0] and j == cliff_state[1]:
                reward = cliff_reward
                break

        return reward

    def get_next_state(self, state, action):
        i, j = state

        if self.is_cliff_state(state):
            next_state = self.get_next_state_cliff(state)
            next_i = next_state[0]
            next_j = next_state[1]
        elif (i, j) in self.TERMINAL_STATES:
            next_i = i
            next_j = j
        else:
            if action == self.ACTION_UP:
                next_i = max(i - 1, 0)
                next_j = j
            elif action == self.ACTION_DOWN:
                next_i = min(i + 1, self.HEIGHT - 1)
                next_j = j
            elif action == self.ACTION_LEFT:
                next_i = i
                next_j = max(j - 1, 0)
            elif action == self.ACTION_RIGHT:
                next_i = i
                next_j = min(j + 1, self.WIDTH - 1)
            else:
                raise ValueError()

        return next_i, next_j

    def get_reward(self, state, next_state):
        i, j = state
        next_i, next_j = next_state

        if self.is_cliff_state(state):
            reward = self.get_reward_cliff(state)
        else:
            if (next_i, next_j) in self.TERMINAL_STATES:
                reward = self.terminal_reward
            else:
                if i == next_i and j == next_j:
                    reward = self.outward_reward
                else:
                    reward = self.transition_reward

        return reward

    def get_state_action_probability(self, state, action):
        next_i, next_j = self.get_next_state(state, action)

        reward = self.get_reward(state, (next_i, next_j))
        transition_prob = 1.0

        return (next_i, next_j), reward, transition_prob

    # take @action in @state
    # @return: (reward, new state)
    def step(self, action):
        next_i, next_j = self.get_next_state(
            state=self.current_state, action=action
        )

        reward = self.get_reward(self.current_state, (next_i, next_j))

        self.current_state = (next_i, next_j)

        if self.current_state in self.TERMINAL_STATES:
            done = True
        else:
            done = False

        return (next_i, next_j), reward, done, None

    def render(self, mode='human'):
        print(self.__str__())

    # 임의의 행동을 선택하여 반환
    def get_random_action(self):
        return random.choice(self.ACTIONS)

    def __str__(self):
        gridworld_str = ""
        for i in range(self.HEIGHT):
            gridworld_str += "-" * 99 + "\n"

            for j in range(self.WIDTH):
                if self.current_state[0] == i and self.current_state[1] == j:
                    gridworld_str += "|   {0}   ".format("*")
                elif (i, j) == self.START_STATE:
                    gridworld_str += "|   {0}   ".format("S")
                elif (i, j) in self.TERMINAL_STATES:
                    gridworld_str += "|   {0}   ".format("G") if j < 10 else "|   {0}    ".format("G")
                elif self.CLIFF_STATES_INFO and (i, j) in [state[0] for state in self.CLIFF_STATES_INFO]:
                    gridworld_str += "|   {0}   ".format("W") if j < 10 else "|   {0}    ".format("W")
                else:
                    gridworld_str += "|       " if j < 10 else "|        "
            gridworld_str += "|\n"

            for j in range(self.WIDTH):
                gridworld_str += "| ({0},{1}) ".format(i, j)

            gridworld_str += "|\n"

        gridworld_str += "-" * 99 + "\n"
        return gridworld_str

def epsilon_scheduled(current_episode):
    fraction = min(current_episode / LAST_SCHEDULED_EPISODES, 1.0)
    epsilon = min(
        INITIAL_EPSILON + fraction * (FINAL_EPSILON - INITIAL_EPSILON),
        INITIAL_EPSILON
    )
    return epsilon

# epsilon-탐욕적 정책 갱신
def update_epsilon_greedy_policy(env, state, q_value, policy, current_episode):
    max_prob_actions = [action_ for action_, value_
                        in enumerate(q_value[state[0], state[1], :]) if
                        value_ == np.max(q_value[state[0], state[1], :])]

    actions = []
    action_probs = []

    epsilon = epsilon_scheduled(current_episode)

    for action in env.ACTIONS:
        actions.append(action)
        if action in max_prob_actions:
            action_probs.append(
                (1 - epsilon) / len(max_prob_actions) + epsilon / env.NUM_ACTIONS
            )
        else:
            action_probs.append(
                epsilon / env.NUM_ACTIONS
            )

    policy[state] = (actions, action_probs)


def sarsa(env, q_value, policy, current_episode, step_size=ALPHA):
    episode_reward = 0.0
    state = env.reset()
    actions, prob = policy[state]
    action = np.random.choice(actions, size=1, p=prob)[0]
    done = False
    while not done:
        next_state, reward, done, _ = env.step(action)
        episode_reward += reward

        # Q-테이블 갱신
        if done:
            q_value[state[0], state[1], action] += step_size * \
                                                   (reward - q_value[state[0], state[1], action])

            update_epsilon_greedy_policy(
                env, state, q_value, policy, current_episode
            )
        else:
            next_actions, prob = policy[next_state]

            next_action = np.random.choice(next_actions, size=1, p=prob)[0]

            next_q = q_value[next_state[0], next_state[1], next_action]

            q_value[state[0], state[1], action] += step_size * \
                                                   (reward + GAMMA * next_q - q_value[state[0], state[1], action])

            update_epsilon_greedy_policy(
                env, state, q_value, policy, current_episode
            )

            state = next_state
            action = next_action

    return episode_reward


def q_learning(env, q_value, policy, current_episode, step_size=ALPHA):
    episode_reward = 0.0
    state = env.reset()
    done = False
    while not done:
        actions, prob = policy[state]
        action = np.random.choice(actions, size=1, p=prob)[0]
        next_state, reward, done, _ = env.step(action)
        # print(state, actions, prob, action, next_state, reward)
        episode_reward += reward

        # Q-테이블 갱신
        if done:
            q_value[state[0], state[1], action] += step_size * \
                                                   (reward - q_value[state[0], state[1], action])

            update_epsilon_greedy_policy(
                env, state, q_value, policy, current_episode
            )
        else:
            # 새로운 상태에 대한 기대값 계산
            max_next_q = np.max(q_value[next_state[0], next_state[1], :])

            q_value[state[0], state[1], action] += step_size * \
                                                   (reward + GAMMA * max_next_q - q_value[state[0], state[1], action])

            update_epsilon_greedy_policy(
                env, state, q_value, policy, current_episode
            )

            state = next_state

    return episode_reward


def expected_sarsa(env, q_value, policy, current_episode, step_size=ALPHA):
    episode_reward = 0.0
    state = env.reset()
    done = False
    while not done:
        actions, prob = policy[state]
        action = np.random.choice(actions, size=1, p=prob)[0]
        next_state, reward, done, _ = env.step(action)
        episode_reward += reward

        # Q-테이블 갱신
        if done:
            q_value[state[0], state[1], action] += step_size * \
                                                   (reward - q_value[state[0], state[1], action])

            update_epsilon_greedy_policy(env, state, q_value, policy, current_episode)
        else:
            # 새로운 상태에 대한 기대값 계산
            expected_next_q = 0.0

            for action_ in env.ACTIONS:
                action_prob = policy[next_state][1]
                expected_next_q += action_prob[action_] * \
                                   q_value[next_state[0], next_state[1], action_]

            q_value[state[0], state[1], action] += step_size * \
                                                   (reward + GAMMA * expected_next_q - q_value[
                                                       state[0], state[1], action])

            update_epsilon_greedy_policy(
                env, state, q_value, policy, current_episode
            )

            state = next_state

    return episode_reward

def td_epsilon_scheduled_comparison(env):
    rewards_expected_sarsa = np.zeros(MAX_EPISODES)
    rewards_sarsa = np.zeros(MAX_EPISODES)
    rewards_q_learning = np.zeros(MAX_EPISODES)

    # Q-Table 변수 선언
    q_table_sarsa = None
    q_table_q_learning = None
    q_table_expected_sarsa = None

    for run in range(TOTAL_RUNS):
        print("runs: {0}".format(run))

        # 초기 Q-Table 생성
        q_table_sarsa = generate_initial_q_value(env)
        q_table_q_learning = generate_initial_q_value(env)
        q_table_expected_sarsa = generate_initial_q_value(env)

        # 초기 임의 정책 생성
        policy_sarsa = generate_initial_random_policy(env)
        policy_q_learning = generate_initial_random_policy(env)
        policy_expected_sarsa = generate_initial_random_policy(env)

        for episode in range(MAX_EPISODES):
            rewards_sarsa[episode] += sarsa(
                env, q_table_sarsa, policy_sarsa, episode
            )
            rewards_q_learning[episode] += q_learning(
                env, q_table_q_learning, policy_q_learning, episode
            )
            rewards_expected_sarsa[episode] += expected_sarsa(
                env, q_table_expected_sarsa, policy_expected_sarsa, episode
            )

    # 총 10번의 수행에 대해 평균 계산
    rewards_expected_sarsa /= TOTAL_RUNS
    rewards_sarsa /= TOTAL_RUNS
    rewards_q_learning /= TOTAL_RUNS

    # 그래프 출력
    plt.plot(
        rewards_sarsa, linestyle='-', color='darkorange',
        label='SARSA'
    )
    plt.plot(
        rewards_q_learning, linestyle=':', color='green',
        label='Q-Learning'
    )
    plt.plot(
        rewards_expected_sarsa, linestyle='-.', color='dodgerblue',
        label='Expected SARSA'
    )

    plt.xlabel('Episodes')
    plt.ylabel('Episode rewards')
    plt.ylim([-100, 0])
    plt.legend()

    #plt.savefig('images/cliff_td_scheduled_comparison.png')
    plt.show()
    plt.close()

    # display optimal policy
    print()

    print('[SARSA의 학습된 Q-Table 기반 탐욕적 정책]')
    print_optimal_policy(env, q_table_sarsa)

    print('[Q-Learning의 수렴된 Q-Table 기반 탐욕적 정책]')
    print_optimal_policy(env, q_table_q_learning)

    print('[기대값 기반 SARSA의 수렴된 Q-Table 기반 탐욕적 정책]')
    print_optimal_policy(env, q_table_expected_sarsa)

def td_epsilon_scheduled_comparison_main():
    env = CliffGridWorld(
        height=GRID_HEIGHT,
        width=GRID_WIDTH,
        start_state=START_STATE,
        terminal_states=TERMINAL_STATES,
        transition_reward=-1.0,
        terminal_reward=-1.0,
        outward_reward=-1.0,
        cliff_states_info=[(s, START_STATE, -100.0) for s in CLIFF_STATES]
    )

    td_epsilon_scheduled_comparison(env)

if __name__ == '__main__':
    td_epsilon_scheduled_comparison_main()
