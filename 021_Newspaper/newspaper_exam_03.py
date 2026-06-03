# url : https://mattpy.tistory.com/m/entry/%ED%8C%8C%EC%9D%B4%EC%8D%AC%EC%9C%BC%EB%A1%9C-%EC%9B%B9-%ED%81%AC%EB%A1%A4%EB%A7%81-%EC%89%BD%EA%B2%8C%ED%95%98%EA%B8%B0

import requests
from bs4 import BeautifulSoup


url = "https://news.naver.com/main/ranking/popularDay.naver"

# header 설정 없이 그냥 요청하면 네이버에서 차단합니다. 아마 하도 크롤링하는 사람들이 많아서 막은 거 같습니다.
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'
}

# 요청 시작
r = requests.get(url, headers=headers)

# 랭킹페이지 파싱
soup = BeautifulSoup(r.text, "html.parser")

# 각 언론사별 카드형 박스 수집
ranking_boxes = soup.find_all("div", "rankingnews_box")

# 일단 기사 제목만 모아보자.
ranking_news_titles = []

for ranking_box in ranking_boxes:
    article_list = ranking_box.find("ul", "rankingnews_list").find_all("li")
    for arti in article_list:
        content = arti.find("div", "list_content")
        # 각 언론사별로 기사 제목 수집해서 ranking_news_titles에 삽입
        if content:
            ranking_news_titles.append(content.find("a").text.strip())

# 기사 제목 출력
for title in ranking_news_titles:
    print(title)