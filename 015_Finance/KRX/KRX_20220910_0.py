# KRX 개별종목시세 크롤링 1995.05.02 ~ 현재
# 모듈 불러오기
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import os

item_list = ["005930/삼성전자", "003550/LG", "005380/현대차", "089010/켐트로닉스"]
#print(date_list)
download_folder_path = r"D:/Users/MU/Downloads"
file_path = r"D:/Works/PycharmProjects/001_TRAINING/015_Finance/KRX/개별종목시세추이수집"
before_file_list = set(os.listdir(download_folder_path))

driver = webdriver.Chrome("D:/Works/PycharmProjects/001_TRAINING/015_Finance/KRX/chromedriver.exe")

url = "http://data.krx.co.kr/contents/MDC/MDI/mdiLoader/index.cmd?menuId=MDC0201020101"
driver.get(url)
WebDriverWait(driver, 20000).until(EC.invisibility_of_element_located((By.CLASS_NAME, 'loading-bar-overlay')))

item_element = driver.find_element(By.ID, "tboxisuCd_finder_stkisu0_1")
item_search_button = driver.find_element(By.ID, "btnisuCd_finder_stkisu0_1")
start_date_element = driver.find_element(By.ID, "strdDd")
current_date_element = driver.find_element(By.ID, "endDd")
search_button = driver.find_element(By.ID, "jsSearchButton")

#for item in item_list:
#    print(item)
#    item_element.click()
#    driver.execute_script("arguments[0].value = '{}'".format(item), item_element)
#    item_search_button.click()
#    driver.execute_script("arguments[0].value = '{}'".format(19950502), start_date_element)
#    search_button.click()
#    driver.execute_script("arguments[0].value = '{}'".format(20220908), current_date_element)
#    search_button.click()
#    download_button = WebDriverWait(driver, 300).until(lambda x: x.find_element(By.CLASS_NAME, "CI-MDI-UNIT-DOWNLOAD"))
#    download_button.click()
#    csv_button = WebDriverWait(driver, 1000).until(lambda x: x.find_element(By.XPATH, '/html/body/div[2]/section[2]/section/section/div/div/form/div[2]/div[2]/div[2]/div/div[2]/a'))
#    csv_button.click()

    # 다운로드될 때까지 기다리기(= 폴더 내 파일 개수가 일치하지 않을 때까지 기다리기)
#    while True:
#        if len(before_file_list) != len(os.listdir(download_folder_path)):
#            new_file = (set(os.listdir(download_folder_path)) - before_file_list).pop()
#            if '.csv' in new_file:
#                break
#    os.rename(download_folder_path + "/" + new_file, file_path + "/" + date + ".csv")
#    before_file_list = set(os.listdir(download_folder_path))
