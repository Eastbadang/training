# pip install pyserial

#-*- coding:utf-8 -*-

import serial
import time

ser = serial.Serial(
    port='COM6',  # COM Port 확인(장치관리자)
    baudrate=115200,
    parity=serial.PARITY_NONE,
    stopbits=serial.STOPBITS_ONE,
    bytesize=serial.EIGHTBITS,
    timeout=1)

print(ser.portstr)  # 연결된 포트 확인

#ser.write(bytes('1+2',encoding='ascii'))
#ser.write(b'1+2')
#ser.write(b'\xff\xfe\xaa')

#vals = [12, 0, 0, 0, 0, 0, 0, 0, 7, 0, 36, 100]
#ser.write(bytearray(vals))
#if ser.readable():
#    res = ser.readline()
#print(res.decode()[:len(res)-1])

ser.write(b'\x01\x05A\x01print(123)\x04')

print(ser.readline())

ser.close()

