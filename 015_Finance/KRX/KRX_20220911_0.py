# https://github.com/sharebook-kr/pykrx
# pip install pykrx
# DB 구성 포함

from pykrx import stock
# from pykrx import bond        # import 오류
import time                     # 시간지연함수 사용

# 코스피
#tickers = stock.get_market_ticker_list("20220908")
#print(tickers)
#print(len(tickers))

#tickers = stock.get_market_ticker_list()
#print(tickers)
#print(len(tickers))


# market : KOSPI, KOSDAQ, KONEX
#tickers = stock.get_market_ticker_list("20220908", market="KOSDAQ")
#print(tickers)
#print(len(tickers))

#for ticker in tickers:
#    종목 = stock.get_market_ticker_name(ticker)
#    print(ticker, 종목)

# OHLCV
#df = stock.get_market_ohlcv("19950502", "20220908", "005930")
#print(df.head(3))

# frequency parameter : d/m/y
#df = stock.get_market_ohlcv("19950502", "20220908", "005930", "m")
#print(df.head(3))


#for ticker in stock.get_market_ticker_list():
#    df = stock.get_market_ohlcv("19950502", "20220908", ticker)
#    print(df.head())
#    time.sleep(1)

df = stock.get_market_ohlcv("19950502", "20220908", "005930")     # 19950502 ~ 20220908 = 6925
#print(len(df.head(10000)))

time.sleep(1)

