# https://www.tensorflow.org/tutorials/quickstart/beginner?hl=ko

import tensorflow as tf

mnist = tf.keras.datasets.mnist

# MNIST 데이터셋 로드 준비, 샘플 값을 정수에서 부동소수로 변환
(x_train, y_train), (x_test, y_test) = mnist.load_data()
x_train, x_test = x_train / 255.0, x_test / 255.0

# 층을 차례대로 쌓아 tf.keras.Sequential 모델
model = tf.keras.models.Sequential([
  tf.keras.layers.Flatten(input_shape=(28, 28)),
  tf.keras.layers.Dense(128, activation='relu'),
  tf.keras.layers.Dropout(0.2),
  tf.keras.layers.Dense(10, activation='softmax')
])

# 훈련에 사용할 옵티마이저와 손실 함수 선택
model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

# 모델 훈련 평가
model.fit(x_train, y_train, epochs=5)
model.evaluate(x_test,  y_test, verbose=2)

