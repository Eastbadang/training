# https://wantfree.tistory.com/575

import feedparser
from newspaper import Article

#검색할 뉴스페이지
rss_url = ["http://rss.etnews.com/Section901.xml",
        # "http://rss.etnews.com/Section902.xml",
        # "http://rss.etnews.com/Section903.xml",
        # "http://biz.heraldm.com/rss/010000000000.xml",
        # "http://media.daum.net/rss/today/primary/all/rss2.xml",
        None]

#rss_urls를 받아 title과 link를 담아둔 rss_dic를 반환한다.
def news_rss(rss_url):
    rss_dic = []
    for rss in rss_url:
        if rss == None:
            break
        else:
            print(rss,"parsing...")
            parse_rss = feedparser.parse(rss)
            print(rss,"complete..")
            for p in parse_rss.entries:
                rss_dic.append({'title':p.title, 'link':p.link})
        return rss_dic

#news의 url을 입력받아, 제목과 기사내용을 반환하는 함수 crawl_news작성
def crawl_news(url, language = 'ko'):
    #Article 함수를 사용하여 받아온 url을 parsing하여 news_article에 넣기
    news_article = Article(url,languages=language)
    news_article.download()
    news_article.parse()
    #news_article의 title과 text를 반환
    return news_article.title, news_article.text

def main():
    print('<<<parsing news titles>>>')
    news_list = news_rss(rss_url)
    print('<<<[completed] parsing news titles>>>')
    print(news_list)
    #crawl_news함수를 활용하여 text/ title을 가져와 넣어주기
    print('<<<crawlling news>>>')
    for news in news_list:
        title, text = crawl_news(news['link'])
        news['title'] = title
        news['text'] =text
    print('<<<[completed]crawlling news>>>')
    print(news_list[0]['text'][:20]) # 내용이 길기때문에 리스트에 있는 0번째 기사의 내용중 20자만 프린트해보자

if __name__ == "__main__":
    main()

from konlpy.tag import Okt
from collections import Counter

splt = Okt()
#기사내용중 한문장으로 테스트
sentence = """SK텔링크가 태평양 횡단 경로에 최초로 패킷 기반 전송 네트워크를 구축, 세계적 통신사업자로 나아가고
있다.
SK텔링크는 지난해 출시한 시에나(Ciena) 어댑티브 IP 솔루션을 도입해 태평양 횡단 해저 네트워크를 업그레이드하고 차
별화된 고객경험을 제공하는 플랫폼을 구축한다고 5일 밝혔다.
'글로벌 IT 선도 기업'을 추구하는 SK텔링크는 세계 각국 고객에게 통신 서비스를 편리하고 안전하게 제공할 수 있는 환
경을 조성하고 있다. 서울, 홍콩, LA를 연결하는 자사 해저 네트워크에 시에나 어댑티브 IP 솔루션을 도입해 통합형 패
킷 네트워크를 구축, 차세대 IP 기반 서비스로 나아가는 발판을 마련할 계획이다.
회사는 시에나 어댑티브 IP 솔루션 기능 중 하나인 시에나 6500 패킷전송시스템(PTS)을 운용해 기존 시분할 다중 방식
네트워크를 지원하고 장비운영 규모와 전력소비를 줄인다. 또 시에나 관리·제어·계획(MCP) 도메인 컨트롤러로 신속
한 네트워크·서비스 관리를 지원해 SK텔링크의 패킷 네트워크 수명주기 운영을 자동화한다.
SK텔링크는 이를 계기로 새로운 수준의 확장성, 유연성, 프로그래밍 가능성을 달성해 고속 인터넷·클라우드 서비스를
효율적으로 전달할 수 있을 것으로 기대하고 있다.
이정열 SK텔링크 ICT인프라본부장은 “최근 급속도로 빨라지고 있는 고객의 데이터 소비 수요에 대응하기 위해 시에나
솔루션으로 태평양 횡단 경로에 패킷기반 전송 네트워크 중 하나를 처음 구축했다”면서 “'미래를 생각하는 세계적
통신사업자'가 되고자 하는 SK텔링크의 비전을 실현하고 '세계 최고 통신 서비스를 제공하겠다'는 고객과 약속을 실현
할 수 있을 것”이라고 말했다.
최근 5세대(G) 이동통신, 사물인터넷(IoT), 인공지능(AI) 등 디지털 혁명으로 더 간단하고 효과적 방식으로 네트워크를
확장할 수 있도록 IP 네트워크를 재구성해 달라는 고객 수요가 급증하고 있다. 이에 시에나는 지난해 어댑티브 IP 솔루
션을 출시, 끊임없이 변화하는 최종 사용자 요구에 대응 가능한 어댑티드 네트워크 구축을 돕는 솔루션을 고객에게 제
공하고 있다.
김인성 시에나 한국지사장은 “한국 정부가 포스트 코로나 시대를 대비해 디지털 뉴딜 카드를 꺼내들었고 SK텔링크 또
한 한국의 새로운 디지털 성장에 대비하고 있다”면서 “시에나의 패킷 솔루션은 변화하는 고객 수요에 실시간 대응할
수 있는 네트워크 환경을 조성하기 위한 기반이 될 것”이라고 전했다.
"""
noun = splt.nouns(sentence)
pos = splt.pos(sentence)

print("<<<noun>>>",noun)
print("<<<pos>>>",pos)

count = Counter(noun)
print(count)

count.most_common(50)