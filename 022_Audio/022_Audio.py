# https://fast-it.tistory.com/entry/%ED%8C%8C%EC%9D%B4%EC%8D%AC%EC%9C%BC%EB%A1%9C-%EC%9D%8C%EC%84%B1%EC%9D%B8%EC%8B%9D-%EB%B4%87-%EB%A7%8C%EB%93%A4%EA%B8%B01

import speech_recognition as sr

Recognizer = sr.Recognizer()  # 인스턴스 생성
mic = sr.Microphone()
with mic as source:  # 안녕~이라고 말하면
    audio = Recognizer.listen(source)
try:
    data = Recognizer.recognize_google(audio, language="ko")
except:
    print("이해하지 못했음")

print(data)  # 안녕 출력