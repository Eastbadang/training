# url : https://kejdev.tistory.com/71

import urllib.request as rq
from bs4 import BeautifulSoup
from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt
from os import path
import re

def start(url):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36',}
    url = rq.Request(url, headers = headers)
    res = rq.urlopen(url).read()
    return BeautifulSoup(res, "html.parser")

def fetch_list_url(url, tag):
    global result
    soup = start(url)
    for link in soup.select(tag[0]):
        result.append(link.get_text())
        print('link =', link['href'], link.get_text())
        news_fetch(link['href'], tag)

def news_fetch(url, tag):
    soup = start(url)
    for link in soup.select(tag[1]):
        result.append(link.get_text())

result = []
search_text = str(input("검색어를 입력하세요 : ").encode("utf-8"))[2:-1].replace('\\x', '%')

def numbers_to_strings():
    # 2022-02-03 확인
    # https://search.daum.net/search?w=news&DA=STC&enc=utf8&cluster=y&cluster_page=1&q=%EC%9D%B8%EA%B3%B5%EC%A7%80%EB%8A%A5&cpname=%EC%A0%84%EC%9E%90%EC%8B%A0%EB%AC%B8&cp=16sIQ8rx97vi9RHx8w&p=1
    # https://search.daum.net/search?w=news&DA=STC&enc=utf8&cluster=y&cluster_page=1&q=%EC%9D%B8%EA%B3%B5%EC%A7%80%EB%8A%A5&cpname=%EB%94%94%EC%A7%80%ED%84%B8%ED%83%80%EC%9E%84%EC%8A%A4&cp=16_-rXIov6CN5sdGtY&p=1
    # https://search.daum.net/search?w=news&DA=STC&enc=utf8&cluster=y&cluster_page=1&q=%EC%9D%B8%EA%B3%B5%EC%A7%80%EB%8A%A5&cpname=%EA%B2%BD%ED%96%A5%EC%8B%A0%EB%AC%B8&cp=16akMkKFDu6n8GTzZr&p=1
    # https://search.daum.net/search?w=news&DA=STC&enc=utf8&cluster=y&cluster_page=1&q=%EC%9D%B8%EA%B3%B5%EC%A7%80%EB%8A%A5&cpname=%EC%A4%91%EC%95%99%EC%9D%BC%EB%B3%B4&cp=16Elf9uX5H6T5xXvQV&p=1
    # https://search.daum.net/search?w=news&DA=STC&enc=utf8&cluster=y&cluster_page=1&q=%EC%9D%B8%EA%B3%B5%EC%A7%80%EB%8A%A5&cpname=%EB%8F%99%EC%95%84%EC%9D%BC%EB%B3%B4&cp=16bOiOx4gG2S18EPLj&p=1
    # https://search.daum.net/search?w=news&DA=STC&enc=utf8&cluster=y&cluster_page=1&q=%EC%9D%B8%EA%B3%B5%EC%A7%80%EB%8A%A5&cpname=%EC%A1%B0%EC%84%A0%EC%9D%BC%EB%B3%B4&cp=16d4PV266g2j-N3GYq&p=1
    num = input('1 : 전자신문 \n2 : 디지털 타임즈 \n3 : 경향신문 \n4 : 중앙일보 \n5 : 동아일보 \n6 : 조선일보\n')
    switcher = {
        1: ['https://search.daum.net/search?w=news&DA=STC&enc=utf8&cluster=y&cluster_page=1&q={search}&cpname=%EC%A0%84%EC%9E%90%EC%8B%A0%EB%AC%B8&cp=16sIQ8rx97vi9RHx8w&p={page}',
            ["#newsColl > div.cont_divider > ul > li:nth-child(1) > div.wrap_cont > a", "#articleBody > p"]],
        2: ['https://search.daum.net/search?w=news&DA=STC&enc=utf8&cluster=y&cluster_page=1&q={search}&cpname=%EB%94%94%EC%A7%80%ED%84%B8%ED%83%80%EC%9E%84%EC%8A%A4&cp=16_-rXIov6CN5sdGtY&p={page}',
            ["#newsColl > div.cont_divider > ul > li:nth-child(1) > div.wrap_cont > a", "#articleBody > p"]],
        3: ['https://search.daum.net/search?w=news&DA=STC&enc=utf8&cluster=y&cluster_page=1&q={search}&cpname=%EA%B2%BD%ED%96%A5%EC%8B%A0%EB%AC%B8&cp=16akMkKFDu6n8GTzZr&p={page}',
            ["#newsColl > div.cont_divider > ul > li:nth-child(1) > div.wrap_cont > a", "#container > div.main_container > div.art_cont > div.art_body > p"]],
        4: ['https://search.daum.net/search?w=news&DA=STC&enc=utf8&cluster=y&cluster_page=1&q={search}&cpname=%EC%A4%91%EC%95%99%EC%9D%BC%EB%B3%B4&cp=16Elf9uX5H6T5xXvQV&p={page}',
            ["#newsColl > div.cont_divider > ul > li:nth-child(1) > div.wrap_cont > a" ,"#article_body"]],
        5: ['https://search.daum.net/search?w=news&DA=STC&enc=utf8&cluster=y&cluster_page=1&q={search}&cpname=%EB%8F%99%EC%95%84%EC%9D%BC%EB%B3%B4&cp=16bOiOx4gG2S18EPLj&p={page}',
            ["#newsColl > div.cont_divider > ul > li:nth-child(1) > div.wrap_cont > a" , "div.article_txt "]],
        6: ['https://search.daum.net/search?w=news&DA=STC&enc=utf8&cluster=y&cluster_page=1&q={search}&cpname=%EC%A1%B0%EC%84%A0%EC%9D%BC%EB%B3%B4&cp=16d4PV266g2j-N3GYq&p={page}',
            ["#newsColl > div.cont_divider > ul > li:nth-child(1) > div.wrap_cont > a","div.par"]]
    }
    return switcher.get(int(num), "nothing")

url_list = numbers_to_strings()
for i in range(1, 10):
    url, tag = url_list[0].format(search=search_text, page=i), url_list[1]
    fetch_list_url(url, tag)

print(result)

f = open('data3.txt', 'w', encoding='UTF-8')
f.writelines(result)
f.close()

