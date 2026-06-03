import os, sys, time
from win32com.client import GetObject

WMI = GetObject('winmgmts:')

ProcessList = []
processes = WMI.instancesOf('Win32_Process')

for process in processes:
    ProcessList.append(process.Properties_('Name').Value)

print(ProcessList)
