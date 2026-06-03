from gtts import gTTS
import os
import speech_recognition as sr

def speak(text ,lang="ko", speed=False):
    tts = gTTS(text=text, lang=lang , slow=speed)
    tts.save("./tts.mp3")
    os.system("afplay " + "./tts.mp3")

Recognizer = sr.Recognizer()
mic = sr.Microphone()

while True:
    with mic as source:
        audio = Recognizer.listen(source)
    try:
        data = Recognizer.recognize_google(audio ,language="ko")
    except:
        speak("이해하지 못하는 말이에요")
    print(data)
    if "에리스" in data or "엘리스" in data or "앨리스" in data:
        speak("넹")
        print("에리스 : 넹")
    else:
        speak("다시 불러주세요")