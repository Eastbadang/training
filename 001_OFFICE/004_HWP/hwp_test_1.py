# package 설치
# pip install pywin32

from time import sleep

import pyperclip as cb
import pandas as pd
from selenium import webdriver
import win32com.client as win32

driver = webdriver.Chrome(r"./chromedriver.exe")
driver.get('http://dart.fss.or.kr/dsac001/mainAll.do')

# onclick_list = []
# for i in driver.find_elements_by_css_selector('a[href^="/dsaf001/main.do?rcpNo="]'):
#     onclick_list.append(i.get_attribute('onclick'))

onclick_list = [i.get_attribute('onclick') for i in driver.find_elements_by_css_selector('a[href^="/dsaf001/main.do?rcpNo="]')]
onclick_list[:5]

link_list = []

for i in onclick_list[:5]:
    driver.execute_script(i)
    driver.switch_to.window(driver.window_handles[1])
    driver.execute_script(driver.find_element_by_css_selector('a[href="#download"]').get_attribute('onclick'))
    driver.switch_to.window(driver.window_handles[2])
    current_len = len(link_list)
    link_list.append(driver.find_element_by_css_selector('a[href^="/pdf"]').get_attribute('href'))

    while True:
        if len(link_list) != current_len:
            break
        else:
            sleep(0.1)
    print(link_list[-1])

    driver.close()
    driver.switch_to.window(driver.window_handles[1])
    driver.close()
    driver.switch_to.window(driver.window_handles[0])

# 너무 오래 걸리는 관계로...
import pickle

with open(r"D://Works//PycharmProjects//001_TRAINING//001_OFFICE//004_HWP//link_list.pickle", 'rb') as f:
    link_list = pickle.load(f)

link_list[:10]

# driver.page_source
# table = pd.read_html(driver.page_source)
table = pd.read_html(driver.page_source)[0]

driver.close()

table.head()

len(table)

len(table.columns)

hwp = win32.Dispatch('HWPFrame.HwpObject')
hwp.RegisterModule("FilePathCheckDLL", "SecurityModule")  # 보안모듈

hwp.Open(r"D://Works//PycharmProjects//001_TRAINING//001_OFFICE//004_HWP//dart_template.hwp")


def hwp_insert_hyperlink(text, url):
    hwp.HAction.Run("TableCellBlock")
    hwp.HAction.GetDefault("InsertHyperlink", hwp.HParameterSet.HHyperLink.HSet)
    hwp.HParameterSet.HHyperLink.Text = text
    hwp.HParameterSet.HHyperLink.Command = url
    hwp.HAction.Execute("InsertHyperlink", hwp.HParameterSet.HHyperLink.HSet)


def hwp_insert_text(text):
    hwp.HAction.GetDefault("InsertText", hwp.HParameterSet.HInsertText.HSet)
    hwp.HParameterSet.HInsertText.Text = text
    hwp.HAction.Execute("InsertText", hwp.HParameterSet.HInsertText.HSet)


# for i in len(table):
#     for j in table.loc[i]:
#         cb.copy(j)
#         hwp.Run('Paste')
#         hwp.Run('TableRightCellAppend')
#     hwp.Run('TableAppendRow')

# 좀 더 다듬어보면,
for i in range(len(table[:10])):
    for idx, text in enumerate(table.loc[i]):
        if idx == 0 and i == 0:
            hwp_insert_text(text)
        elif idx == 2:  # 보고서명 칼럼, 하이퍼링크를 삽입해야 한다.
            hwp.Run('TableRightCellAppend')
            hwp_insert_hyperlink(text=text, url='{};1;0;0'.format(link_list[i].replace("?", "\\?")))
        elif idx == 5:  # 오른쪽 끝 비고란, 전부 Nan이므로 아무것도 입력하지 않고 넘어간다.
            hwp.Run('TableRightCellAppend')
        else:  # 그 외에는 텍스트를 그대로 입력한다.
            hwp.Run('TableRightCellAppend')
            hwp_insert_text(text)