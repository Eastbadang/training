from gtts import gTTS

text = "나는 운동하는 코린이야!"

tts = gTTS(text=text, lang='ko')
tts.save("hello.mp3")