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
# https://search.naver.com/search.naver?where=news&sm=tab_pge&query=무선충전&sort=0&photo=0&field=0&pd=0&ds=&de=&cluster_rank=24&mynews=0&office_type=0&office_section_code=0&news_office_checked=&nso=so:r,p:all,a:all&start=1
# https://search.naver.com/search.naver?where=news&sm=tab_pge&query={s}&sort=0&photo=0&field=0&pd=0&ds=&de=&cluster_rank=24&mynews=0&office_type=0&office_section_code=0&news_office_checked=&nso=so:r,p:all,a:all&start={p}
# https://search.naver.com/search.naver?where=news&sm=tab_pge&query=무선충전&sort=0&photo=0&field=0&pd=0&ds=&de=&cluster_rank=24&mynews=0&office_type=0&office_section_code=0&news_office_checked=&nso=so:r,p:all,a:all&start=11
for p in range(1, 101, 10):
    raw = requests.get("https://search.naver.com/search.naver?where=news&sm=tab_pge&query={s}&sort=0&photo=0&field=0&pd=0&ds=&de=&cluster_rank=24&mynews=0&office_type=0&office_section_code=0&news_office_checked=&nso=so:r,p:all,a:all&start={p}".format(s = search, p = p))
    html = BeautifulSoup(raw.text, 'html.parser')
    # print(html)
    container = html.select("#main_pack > section.sc_new.sp_nnews._prs_nws > div > div.group_news > ul > li")
    # print(container)

    for c in container:
        # 기사제목
        title = c.select_one('li > div > div:nth-child(1) > a').text.strip()
        # print(title)
        # 기사요약
        content = c.select_one('div.news_wrap.api_ani_send > div > div.news_dsc > div > a').text.strip()
        # print(content)
        # 신문사
        comp = c.select_one('div.news_wrap.api_ani_send > div > div.news_info > div.info_group > a.info.press').text.replace('언론사 선정','')
        # print(comp)
        # 기사url
        url = c.select_one('li > div > div:nth-child(1) > a')['href']
        # print(url)
        ws1.append([title, content, comp, url])

wb.save('naver_news.xlsx')

