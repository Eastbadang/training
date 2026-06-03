# https://creatorjo.tistory.com/86
# https://creatorjo.tistory.com/87
# https://creatorjo.tistory.com/88

from bs4 import BeautifulSoup
from selenium import webdriver
from openpyxl import Workbook
from openpyxl.utils import get_column_letter
from openpyxl.drawing.image import Image
import dload

driver = webdriver.Chrome('chromedriver')

url = "https://search.naver.com/search.naver?where=news&sm=tab_jum&query=무선충전"

driver.get(url)
req = driver.page_source
soup = BeautifulSoup(req, 'html.parser')
# print(soup)

# https://search.naver.com/search.naver?where=news&sm=tab_pge&query=%EC%A3%BC%EC%8B%9D&sort=0&photo=0&field=0&pd=0&ds=&de=&cluster_rank=84&mynews=0&office_type=0&office_section_code=0&news_office_checked=&nso=so:r,p:all,a:all&start=1
# https://search.naver.com/search.naver?where=news&sm=tab_pge&query=%EC%A3%BC%EC%8B%9D&sort=0&photo=0&field=0&pd=0&ds=&de=&cluster_rank=67&mynews=0&office_type=0&office_section_code=0&news_office_checked=&nso=so:r,p:all,a:all&start=11
# https://search.naver.com/search.naver?where=news&sm=tab_pge&query=%EC%A3%BC%EC%8B%9D&sort=0&photo=0&field=0&pd=0&ds=&de=&cluster_rank=109&mynews=0&office_type=0&office_section_code=0&news_office_checked=&nso=so:r,p:all,a:all&start=21

# 기사 셀렉터
articles = soup.select('#main_pack > section.sc_new.sp_nnews._prs_nws > div > div.group_news > ul > li')
# print(articles)

# 엑셀로 저장하기 세팅
wb = Workbook()
ws1 = wb.active
ws1.title = "네이버 주식 기사 스크래핑"
ws1.append(["제목", "링크", "신문사", "썸네일", "썸네일 이미지"])
ws1.column_dimensions['E'].width = 33

for k in range(1, 11):
    ws1.row_dimensions[k+1].height = 150

i = 1
# 한 페이지 내에 있는 기사 제목, url, 신문사 이름, 썸네일 스크래핑
#main_pack > section.sc_new.sp_nnews._prs_nws > div > div.group_news > ul
for article in articles:
    # print(article)
    # 기사 스크래핑
    a_tag = article.select_one('li > div > div:nth-child(1) > a')
    # a_tag = article.find('a', class_='news_tit')
    # print(a_tag.text)

    # 제목 텍스트 스크래핑
    title = a_tag.text
    # print(title)

    # url스크래핑
    url = a_tag['href']
    # print(url)

    # 신문사이름스크래핑
    # sp_nws1 > div.news_wrap.api_ani_send > div > div.news_info > div.info_group > a.info.press
    comp = article.select_one('div.news_wrap.api_ani_send > div > div.news_info > div.info_group > a.info.press')
    # length = len(comp.text)
    # print(length)
    # comp = comp.text[0:-6]
    comp = comp.text.replace('언론사 선정','')
    # print(comp)

    # 썸네일 스크래핑
    # sp_nws1 > div > a > img
    # sp_nws2 > div > a > img
    # sp_nws3 > div.news_wrap.api_ani_send > a > img
    # sp_nws8 > div > a > img
    # thumbnail = article.select_one('#sp_nws1 > div > a')['src']
    thumbnail = article.select_one('li > div > a > img')['src']
    # thumbnail = article.find('img', class_='thumb api_get')
    dload.save(thumbnail, f'news_img/{i}.jpg')
    # print(thumbnail)

    # 엑셀에 title, url, comp를 저장하기
    # thumbnail 이미지 엑셀 삽입 처리 추가
    img = Image(f'news_img/{i}.jpg')
    ws1.append([title, url, comp, thumbnail])
    ws1.add_image(img, f'E{i+1}')
    i += 1

driver.quit()
wb.save(filename='네이버 기사 스크래핑.xlsx')
