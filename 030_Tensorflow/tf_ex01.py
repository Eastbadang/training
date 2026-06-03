# 텐서플로우는 공개버전은 파이썬 3.7까지만 지원
# 3.8은 유료버전

# conda update -n base conda
# conda update --all
# pip install tensorflow
# or
# pip install --upgrade tensorflow-cpu
# conda install tensorflow

# https://www.tensorflow.org/tutorials/quickstart/beginner?hl=ko

# gpu - amd 라면
# pip uninstall keras
# pip install keras==2.2.2
# pip install plaidml-keras plaidbench
# plaidml-setup


import tensorflow as tf

hello = tf.constant('Hello, TensorFlow!')
sess = tf.Session()   # Error, 텐서플로우 업그레이드 후 방식 변경 
print(sess.run(hello))
a=tf.constant(10)
b=tf.constant(32)
print(sess.run(a+b))
