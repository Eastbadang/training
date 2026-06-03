# -*- coding: utf-8 -*-
import os, sys
import subprocess
import threading
import time
# 원격 서버의 프로그램 실행
svr="ip"
acc="username"
program_path='~/dev/python/remote_run'
args=['LOADER1','LOADER2','LOADER3']
#http://stackoverflow.com/questions/14533458/python-threading-multiple-bash-subprocesses
## 여러대의 장비의 shell 프로세스를 실행(동시에)
print ('use threading...')
# thread class to run a command
class ExampleThread(threading.Thread):
    def __init__(self, cmd):
        threading.Thread.__init__(self)
        self.cmd=cmd
    def run(self):
        # execute the command, queue the result
        ret = subprocess.call(self.cmd, shell=False)
for host in args:
    cmd=["ssh", acc+'@'+svr, program_path+'/'+'stop.sh'+' '+host]
    thread=ExampleThread(cmd)
    thread.start()