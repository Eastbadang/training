import tensorflow as tf
import numpy as np


class QNetwork:
    def __init__(self, learning_rate=0.01, state_size=1,
                 action_size=1, hidden_size=10, name='QNetwork'):
        self.learning_rate = learning_rate
        with tf.variable_scope(name):
            self.inputs_ = tf.placeholder(tf.float32, [None, state_size], name='inputs')
            self.actions_ = tf.placeholder(tf.float32, [None, action_size], name='actions')
            self.targetQs_ = tf.placeholder(tf.float32, [None], name='target')
            self.fc1 = tf.contrib.layers.fully_connected(self.inputs_, hidden_size)
            self.fc2 = tf.contrib.layers.fully_connected(self.fc1, hidden_size)
            self.output = tf.contrib.layers.fully_connected(self.fc2, action_size, activation_fn=None)

            # Q is our predicted Q value.
            self.Q = tf.reduce_sum(tf.multiply(self.output, self.actions_), axis=1)

            # The loss is the difference between our predicted Q_values and the Q_target
            # Sum(Q_target - Q)^2
            self.loss = tf.reduce_mean(tf.square(self.targetQs_ - self.Q))
            self.optimizer = tf.train.AdamOptimizer(self.learning_rate).minimize(self.loss)


def q_learning(sess, env, qnetwork, num_episodes=1000,
               max_steps_per_episode=1000,
               replay_memory_size=50000,
               replay_memory_init_size=5000,
               update_target_every=1000,
               discount_factor=0.9,
               epsilon_start=1.0,
               epsilon_end=0.01,
               epsilon_decay_steps=500):
    """
    Q-Learning algorithm for off-policy TD control using Function Approximation.
    Finds the optimal greedy policy while following an epsilon-greedy policy.
    You can use this function to train the agent.
    :param sess: TensorFlow session
    :param env: OpenAI Gym environment
    :param qnetwork: QNetwork instance
    :param num_episodes: Number of episodes to run for
    :param max_steps_per_episode: Maximum number of steps per episode.
    If the agent takes longer than this many steps to reach the terminal state,
    the episode will be terminated and considered "bad"
    :param replay_memory_size: Size of the replay memory
    :param replay_memory_init_size: Number of random experiences to sample when initializing
    the replay memory.
    :param update_target_every: Update the target network every `update_target_every` episodes.
    :param discount_factor: Gamma discount factor
    :param epsilon_start: Starting value of epsilon for the epsilon-greedy policy
    :param epsilon_end: Final value of epsilon for the epsilon-greedy policy
    :param epsilon_decay_steps: Number of steps to decay epsilon over
    """

    # The replay memory stores tuples (S, A, R, S', done)
    replay_memory = []

    # Create a queue for summing rewards over the last REWARD_QUEUE_SIZE episodes
    reward_queue = deque(maxlen=REWARD_QUEUE_SIZE)

    # Keep track of useful statistics
    stats = plotting.EpisodeStats(
        episode_lengths=np.zeros(num_episodes),
        episode_rewards=np.zeros(num_episodes),
        average_q=np.zeros(num_episodes))

    # Initialize variables
    sess.run(tf.global_variables_initializer())
