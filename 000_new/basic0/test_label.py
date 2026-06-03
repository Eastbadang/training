import tkinter

window = tkinter.Tk() # 루트 윈도우 생성(GUI 객체 생성)

label = tkinter.Label(window, text = "Hello World!") # 라벨 위젯
label.pack() # 위젯 위치를 적당한 곳에 위치시킨다.(auto)

window.mainloop() # Event loop 시작시켜 GUI를 활성화 시킨다.