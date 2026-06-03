# 1. 네이버 증권 기볼 설정 외 항목 결과
# 2. Flask 기초
# 3. 웹 상에서 크롤링한 데이터 보여주기

# 1. 라이브러리 호출
import requests
from bs4 import BeautifulSoup as bs

# 2. 데이터 요청
base_url = "https://finance.naver.com/sise/field_submit.nhn?menu=market_sum&returnUrl=http://finance.naver.com/sise/sise_market_sum.nhn?sosok=0&fieldIds=quant&fieldIds=ask_buy&fieldIds=market_sum&fieldIds=per&fieldIds=ask_sell&fieldIds=roe"
req = requests.get(base_url)
html = req.text
soup = bs(html, "lxml")

#print(soup)

# 3. 데이터 파싱
headers = soup.select("#contentarea > div.box_type_l > table.type_2 > thead > tr > th")
headers = list(map(lambda x: x.text, headers))
print(headers)

stock_datas = soup.select("#contentarea > div.box_type_l > table.type_2 > tbody > tr")  # 공통 주소
for data in stock_datas:
    try:
        stock_rank = data.select_one("td.no").text
        stock_name = data.select_one("td:nth-child(2) > a").text
        stock_price = data.select_one("td:nth-child(3)").text
        stock_quant = data.select_one("td:nth-child(7)").text
        stock_ask_buy = data.select_one("td:nth-child(8)").text
        stock_ask_sell = data.select_one("td:nth-child(9)").text
        stock_per = data.select_one("td:nth-child(11)").text
        stock_roe = data.select_one("td:nth-child(12)").text
        print(stock_rank, stock_name, stock_price, stock_quant, stock_ask_buy, stock_ask_sell, stock_per, stock_roe)
    except AttributeError:
        continue

