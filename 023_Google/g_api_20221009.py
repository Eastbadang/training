# https://dataanalytics.tistory.com/entry/%ED%8C%8C%EC%9D%B4%EC%8D%AC-%EA%B5%AC%EA%B8%80-%ED%8A%B8%EB%A0%8C%EB%93%9C-API-%ED%99%9C%EC%9A%A9%ED%95%B4%EB%B3%B4%EA%B8%B0

from pytrends.request import TrendReq
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px

# pip install pytrends 패키지 설치
# pip install plotly 패치키 설치

# hl= host language. tz = timezone
# hl 언어(한국어), tz 한국시간기준
pytrends = TrendReq(hl='ko', tz=540)

# 시간 타임존은 여기에서 찾으면 됩니다.
# https://forbrains.co.uk/internation_tools/earth_timezones?ref=hackernoon.com

#kw_list : 데이터를 가져올 키워드 목록 (한번에 5개 키워드로 제한)
kw_list = ["induction", "smart kitchen"]

# goe : 지리적 위치, timeframe : 관심있는 시간 프레임
pytrends.build_payload(kw_list, cat=0, timeframe='2020-06-01 2022-10-07', geo='KR')
data = pytrends.interest_over_time()
data = data.reset_index()

# Top 20개 데이터만 보기
print(data.head(20))

fig=px.line(data, x='date', y=kw_list, title='구글 검색 트렌드')
fig.show()

# 그래프로 트렌드 보기
plt.figure()
#plt.plot(df.index, df.갤럭시워치4, label='ratio')
#plt.plot(df.index, df.chicken, label='ratio')
#plt.plot(df.index, df.space, label='ratio')
#plt.legend(['갤럭시워치4'])
