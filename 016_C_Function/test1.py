# Ref. : https://kitae0522.tistory.com/entry/Python-%ED%8C%8C%EC%9D%B4%EC%8D%AC%EC%97%90%EC%84%9C-C-%ED%95%A8%EC%88%98-%ED%98%B8%EC%B6%9C%ED%95%B4%EC%84%9C-%EC%82%AC%EC%9A%A9%ED%95%98%EA%B8%B0
# gcc -c test1.c
# gcc -shared -o test1.dll test1.o

from ctypes import cdll
# cdll.LoadLibrary("%절대경로%\\test1.dll")
test1 = cdll.LoadLibrary("D:\\Works\\PycharmProjects\\001_TRAINING\\016_C_Function\\test1.dll")

#from ctypes import *
#test1 = windll.LoadLibrary("D:\\Works\\PycharmProjects\\001_TRAINING\\016_C_Function\\test1.dll")

print(test1.fibo(40))