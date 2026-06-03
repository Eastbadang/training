# don't run.

from ctypes import *
libc = cdll.msvcrt
print(libc)
libc.printf(b'hello world!\n')

from ctypes import cdll
p = cdll.LoadLibrary('p.dll')

# p.dll 파일은 현재 디렉트로 위치에 있거나, path상에 있어야 함
print(sum(x for x in range(100_0000) if p.isprime(x)))