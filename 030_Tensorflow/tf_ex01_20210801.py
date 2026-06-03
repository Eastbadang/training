import tensorflow as tf

tall = 170
foot = 260

a = tf.Variable(0.1)
b = tf.Variable(0.2)

def loss_function():
    predict_value = tall*a+b
    return tf.square(foot - predict_value)

opt = tf.keras.optimizers.Adam(learning_rate=0.1)

for i in range(300):
    opt.minimize(loss_function, var_list=[a, b])
    print(a.numpy(), b.numpy())



