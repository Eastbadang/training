# 다음 링크에서 현재가 가져와서 엑셀에 저장하기
# 시트 : 현재가

# 1. 웹 사이트에 접속 후 URL 확인
# 2. 원하는 정보의 위치를 확인
# 3. 원하는 형태로 출력하도록 프로그래밍 함.


# 1. 라이브러리 호출단계
# from openpyxl import load_workbook
import requests
from bs4 import BeautifulSoup as bs

# 관리할 엑셀 파일
# wb = load_workbook('D:/Works/PycharmProjects/001_TRAINING/015_Finance/daum/daum_finance_20211010.xlsx')
# wb = load_workbook('D:/Works/PycharmProjects/001_TRAINING/015_Finance/daum/daum_finance_20211010.xlsx')

# Daum
# req = request.get("https://finance.daum.net/domestic/all_stocks?market=KOSPI")
# html = req.text
# soup = bs(html, "lxml")

marketType = {
    "KOSPI": "0",
    "KOSDAQ": "1"
}

for market, code in marketType.items():
    for page in range(1, 36):
        # 2. 데이터 요청 단계
        # Naver
        # 택코딩TechCoding 유튜브 참조
        req = requests.get(f"https://finance.naver.com/sise/sise_market_sum.nhn?sosok={code}&page={page}")
        html = req.text
        soup = bs(html, "lxml")
        #print(soup)  # 데이터 확인

        # 3. 데이터 추출(파싱) 단계
        stockContents = soup.select("#contentarea > div.box_type_l > table.type_2 > tbody > tr")
        # print(stockContents)

        for stockContent in stockContents:
            try:
                stockRank = stockContent.select_one("td.no").text
                stockName = stockContent.select_one("td:nth-child(2) > a").text
                stockPrice = stockContent.select_one("td:nth-child(3)").text
                stockCap = stockContent.select_one("td:nth-child(7)").text
                print(f"{market} {stockRank}등 {stockName} 종목의 현재가는 {stockPrice}원이고, 시가총액은 {stockCap}억 원 입니다.")
                # print(stockRank)
                # print(stockName)
                # print(stockPrice)
                # print(stockCap)
            except AttributeError:
                continue

# for sheet_nm in wb.sheetnames:
#    # print('*' * 100)
#    print('시트명:', sheet_nm)
    # sheet = wb[sheet_nm]

# sheet = wb['Sheet3']

# for row_data in sheet.iter_rows(min_row=1):
#    for cell in row_data:
#        print('[', cell.value, ']')
        # print('=' * 100)

# sheet = wb['현재가']
# print(sheet.cell(row=1, column=4).value)

# wb.close()