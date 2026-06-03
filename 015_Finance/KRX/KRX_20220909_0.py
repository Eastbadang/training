# https://gils-lab.tistory.com/56
# KRX 전종목시세 크롤링
# 모듈 불러오기
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import os

date_list = ["20201201", "20201202", "20201203", "20201204"]
#print(date_list)
download_folder_path = r"D:/Users/MU/Downloads"
file_path = r"D:/Works/PycharmProjects/001_TRAINING/015_Finance/KRX/전종목시세데이터수집"
before_file_list = set(os.listdir(download_folder_path))

driver = webdriver.Chrome("D:/Works/PycharmProjects/001_TRAINING/015_Finance/KRX/chromedriver.exe")

url = "http://data.krx.co.kr/contents/MDC/MDI/mdiLoader/index.cmd?menuId=MDC0201020101"
driver.get(url)
WebDriverWait(driver, 20000).until(EC.invisibility_of_element_located((By.CLASS_NAME, 'loading-bar-overlay')))

date_element = driver.find_element(By.ID, "trdDd")
search_button = driver.find_element(By.ID, "jsSearchButton")

for date in date_list:
    print(date)
    date_element.click()
    driver.execute_script("arguments[0].value = '{}'".format(date), date_element)
    search_button.click()
    download_button = WebDriverWait(driver, 300).until(lambda x: x.find_element(By.CLASS_NAME, "CI-MDI-UNIT-DOWNLOAD"))
    download_button.click()
    csv_button = WebDriverWait(driver, 1000).until(lambda x: x.find_element(By.XPATH, '/html/body/div[2]/section[2]/section/section/div/div/form/div[2]/div[2]/div[2]/div/div[2]/a'))
    csv_button.click()

    # 다운로드될 때까지 기다리기(= 폴더 내 파일 개수가 일치하지 않을 때까지 기다리기)
    while True:
        if len(before_file_list) != len(os.listdir(download_folder_path)):
            new_file = (set(os.listdir(download_folder_path)) - before_file_list).pop()
            if '.csv' in new_file:
                break
    os.rename(download_folder_path + "/" + new_file, file_path + "/" + date + ".csv")
    before_file_list = set(os.listdir(download_folder_path))
