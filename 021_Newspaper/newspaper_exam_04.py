# url : https://mattpy.tistory.com/m/entry/%ED%8C%8C%EC%9D%B4%EC%8D%AC%EC%9C%BC%EB%A1%9C-%EC%9B%B9-%ED%81%AC%EB%A1%A4%EB%A7%81-%EC%89%BD%EA%B2%8C%ED%95%98%EA%B8%B0
# url : https://lsjsj92.tistory.com/442

import time
import requests
from bs4 import BeautifulSoup
import pandas as pd
from collections import Counter
from konlpy.tag import Okt

start = time.time()

url = "https://news.naver.com/main/ranking/popularDay.naver"

# header 설정 없이 그냥 요청하면 네이버에서 차단합니다. 아마 하도 크롤링하는 사람들이 많아서 막은 거 같습니다.
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.82 Safari/537.36'
}

# 요청 시작
r = requests.get(url, headers=headers)

# 랭킹페이지 파싱
soup = BeautifulSoup(r.text, "html.parser")

# 각 언론사별 카드형 박스 수집
ranking_boxes = soup.find_all("div", "rankingnews_box")

# 일단 기사 제목만 모아보자.
ranking_news_titles = []

# 각 기사의 링크를 저장할 리스트를 초기화한다.
ranking_news_links = []

for ranking_box in ranking_boxes:
    article_list = ranking_box.find("ul", "rankingnews_list").find_all("li")
    for arti in article_list:
        content = arti.find("div", "list_content")
        # 각 언론사별로 기사 제목 수집해서 ranking_news_titles에 삽입
        if content:
            ranking_news_titles.append(content.find("a").text.strip())
            # 기사 링크 파싱
            # 이런 종류의 링크를 가져오게됨
            # /main/ranking/read.naver?mode=LSD&mid=shm&sid1=001&oid=422&aid=0000512132&rankingType=RANKING
            ranking_news_links.append(content.find("a")["href"])

articles = []
# print(articles)
# 각 기사별 링크를 통해 기사 원문을 가져온다.
for title, link in zip(ranking_news_titles, ranking_news_links):
    # url = f"https://news.naver.com{link}"  # 링크를 완전하게 만든다.
    url = f"{link}"
    # print(url)
    r = requests.get(url, headers=headers)
    time.sleep(0.5)  # 한 번에 너무 많은 요청을 하면 네이버에서 IP를 차단시킬 수도 있다.
    # 이제 기사 원문을 파싱해보자.
    # https://crazyj.tistory.com/80
    soup = BeautifulSoup(r.text, "html.parser")
    # print(soup)
    article_body = soup.find("div", id="newsct_article")
    # print(article_body)
    article_body = article_body.text.strip()
    # print(article_body)
    # 파싱한 원문을 articles에 삽입
    articles.append(
        {
            "title": title,
            "content": article_body
        }
    )

df = pd.DataFrame(articles)
print(df)

#okt = Okt()

#words = []
#for a in articles:
#    words += okt.nouns(a["title"])
#    words += okt.nouns(a["content"])

#print(Counter(words).most_common())
#print(Counter([w for w in words if len(w) > 1]).most_common())

end = time.time()

print('time : %d 분 %f 초' % ((end-start)//60, ((end-start)/60-((end-start)//60))*60))
