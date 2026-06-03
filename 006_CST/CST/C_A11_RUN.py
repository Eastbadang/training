import sys
import time
sys.path.append(r"<PATH_TO_CST_AMD64>/python_cst_libraries")

import cst
print(cst.__file__) # should print '<PATH_TO_CST_AMD64>\python_cst_libraries\cst\__init__.py'

from win32com import client

# CST STUDIO SUITE 시작
oCSTApp = client.Dispatch("CSTStudio.Application")

oProject = oCSTApp.OpenFile("D:/WORKS/PycharmProjects/py38/CST/CST_RUN/PY_EXAM.cst")

# Active oProject

# Close oProject


# 종료 지연
print("Python, time.sleep(25) -> 25초 기다림")
time.sleep(25)  # 25초 기다림
print("Python, time.sleep(5) -> 5초 기다림")
time.sleep(5)  # 2초 기다림
print("Goodby!")

# CST STUDIO SUITE 종료
oCSTApp.Quit()