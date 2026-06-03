# 네이버 주식정보 가져오기
# BeautifulSoup은 HTML 과 XML 파일로부터 데이터를 수집하는 라이브러리
# pip install bs4
# pip install requests
# pip install fake-useragent

from bs4 import BeautifulSoup
import requests
from fake_useragent import UserAgent
from datetime import datetime
import time


def getCode(company_code):
    # company_code : 기업코드
    url = "https://finance.naver.com/item/main.nhn?code=" + company_code
    ua = UserAgent()
    # 헤더 정보 (http 해킷 헤더에 브라우저 정보가 존재하는지 확인할 경우)
    headers = {'User-agent': ua.ie}
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.content, "html.parser")
    return soup


def getPrice(company_code):
    soup = getCode(company_code)
    # no_today = soup.find("p", {"class": "no_today"})
    no_today = soup.select_one('p.no_today')
    # print(no_today) # 출력을 한 다음에 더 세부적인 정보를 파싱처리한다.
    # blind = no_today.find("span", {"class" : "blind"})
    blind = no_today.select_one('span.blind')
    return blind.text


# 증시 기업코드
company_codes = ["030200", "005930", "068270", "035720"]

if __name__ == '__main__':
    now = datetime.now()
    print("-" * 60)
    print(now)
    print("-" * 60)

    for elm in company_codes:
        nowPrice = getPrice(elm)
        print(nowPrice)
    print("-" * 60)

