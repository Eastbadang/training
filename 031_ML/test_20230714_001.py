# 강화학습... 예제, BING 챗GPT 결과

# python으로 y=x^2-5x+6 함수를 강화학습 알고리즘으로 y=0이 되는 x값을 찾는 방법을 알려줘

# 필요한 모듈 임포트
import numpy as np
import random

# 하이퍼파라미터 설정
alpha = 0.1  # 학습률
gamma = 0.9  # 할인율
epsilon = 0.1  # 탐욕 정책 파라미터
num_episodes = 100  # 에피소드 수

# Q 테이블 초기화 (x값의 범위는 -10에서 10까지 1씩 증가한다고 가정)
Q = np.zeros((401, 2))  # 왼쪽으로 이동하거나 오른쪽으로 이동하는 두 가지 행동

# 에피소드 반복
for i in range(num_episodes):
    # 초기 상태 설정 (x값을 -10에서 10 사이의 임의의 정수로 선택)
    state = random.randint(-10, 10)
    # 에피소드 종료 여부
    done = False

    # 한 에피소드 동안 반복
    while not done:
        # 탐욕 정책에 따라 행동 선택 (왼쪽으로 이동하면 0, 오른쪽으로 이동하면 1)
        if random.random() < epsilon:  # 탐색
            action = random.randint(0, 1)
        else:  # 활용
            action = np.argmax(Q[state + 10])  # Q 값이 최대가 되는 행동

        # 행동에 따라 다음 상태 결정 (x값을 1만큼 증가하거나 감소)
        if action == 0:  # 왼쪽으로 이동
            next_state = state - 1
        else:  # 오른쪽으로 이동
            next_state = state + 1

        # 다음 상태의 y값 계산
        #y = next_state ** 2 - 5 * next_state + 6
        y = next_state ** 2 - 15 * next_state + 6
        #y = next_state ** 3 - 10 * next_state ** 2 - 31 * next_state - 30

        print("*")

        # 보상 결정 (-|y| 값)
        reward = -abs(y)

        # Q 테이블 업데이트
        Q[state + 10, action] = Q[state + 10, action] + alpha * (
                    reward + gamma * np.max(Q[next_state + 10]) - Q[state + 10, action])

        # 다음 상태로 이동
        state = next_state

        # y값이 0이면 에피소드 종료
        if y == 0:
            done = True

    # 에피소드 결과 출력
    print(f"에피소드 {i + 1}: x = {state}, y = {y}")

# 학습된 Q 테이블 출력
print("Q 테이블:")
print(Q)
