# pip install pyinstaller

import time

# -*-coding: utf-8 -*-
def add(a, b):
    return a + b;


def writeToTextFile(a):
    fileWriter = open("D:\\WORKS\\PyCharmProjects\\001_TRAINING\\000_new\\compile\\test.txt", 'w')
    fileWriter.write(str(a) + " is writed")


def main():
    writeToTextFile(add(3, 5))
    print("Example")
    time.sleep(15)
    print("Good Bye")

if __name__ == "__main__":
    main()

# pyinstaller pyc_example.py #
# pyinstaller --noconsole --onefile pyc_example.py # 실행파일 하나만 생성