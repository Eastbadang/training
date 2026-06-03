import requests
from bs4 import BeautifulSoup
from openpyxl import Workbook

# 엑셀로 저장하기 세팅
wb = Workbook()
ws1 = wb.active

# 검색어 입력
# search = input('검색할 데이터를 입력해 주세요 : ')
search = '무선충전'

# 데이터 크롤링
ws1.append(['기사제목', '기사요약', '신문사', '기사 url'])

# for 반복문
# https://search.daum.net/search?w=news&nil_search=btn&DA=NTB&enc=utf8&cluster=y&cluster_page=1&q=무선충전&1
# https://search.daum.net/search?1=&w=news&DA=PGD&enc=utf8&cluster=y&cluster_page=1&q=%EB%AC%B4%EC%84%A0%EC%B6%A9%EC%A0%84&p=2
for p in range(1, 10+1, 1):
    raw = requests.get("https://search.daum.net/search?w=news&nil_search=btn&DA=NTB&enc=utf8&cluster=y&cluster_page=1&q={s}&p={p}".format(s = search, p = p))
    html = BeautifulSoup(raw.text, 'html.parser')
    # print(html)
    container = html.select("div.cont_divider > ul > li")
    # print(container)

    for c in container:
        # 기사제목
        title = c.select_one('div.wrap_cont > a').text.strip()
        # 기사요약
        content = c.select_one('div.wrap_cont > p').text.strip()
        # 신문사
        comp = c.select_one('div.wrap_cont > span.cont_info > span:nth-child(1)').text.strip()
        # 기사url
        url = c.select_one('div.wrap_cont > a')['href']
        ws1.append([title, content, comp, url])

wb.save('daum_news.xlsx')

