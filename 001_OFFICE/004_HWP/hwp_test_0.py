# pacakge 설치
# pip install pywin32

import win32com.client as win32
import win32gui
import win32con

hwp = win32.Dispatch('HWPFrame.HWPObject')
hwnd = win32gui.FindWindow(None, '빈 문서 - 한글')
win32gui.ShowWindow(hwnd, win32con.SW_SHOW) # 백그라운드에서 작업 가능
#win32gui.ShowWindow(hwnd, win32con.SW_HIDE) # 백그라운드에서 작업 가능
