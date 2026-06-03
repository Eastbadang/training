import numpy as np

def f(x):
    return x**3 - 10*x**2 - 31*x - 30

def Q_learning():
    alpha = 0.1
    gamma = 0.9
    epsilon = 0.1
    state = np.random.uniform(-10, 10)
    while True:
        if np.random.uniform() < epsilon:
            action = np.random.uniform(-10, 10)
        else:
            action = np.argmax(Q[state])
        next_state = state + action
        reward = f(next_state)
        Q[state][action] += alpha * (reward + gamma * np.max(Q[next_state]) - Q[state][action])
        state = next_state
        if reward == 0:
            break

Q_learning()
