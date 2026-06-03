# https://github.com/sharebook-kr/pykrx
# # pip install pykrx

# 1. 라이브러리 호출
from pykrx import stock
import time


date = "20211101"

# tickers = stock.get_market_ticker_list(date)
# print(tickers)

# tickers = stock.get_market_ticker_list()
# print(tickers)

# tickers = stock.get_market_ticker_list("20190225", market="KOSDAQ")
# print(tickers)

#no = 0
#for ticker in stock.get_market_ticker_list(date, market="ALL"):
#        종목 = stock.get_market_ticker_name(ticker)
#        no = no + 1
#        print(no, ticker, "A"+ticker, 종목)

# df = stock.get_market_ohlcv_by_date("20150720", "20150810", "005930")
# print(df.head(3))

# df = stock.get_market_ohlcv_by_date("20180810", "20181212", "005930", "m")
# print(df.head(3))

# stock.get_stock_ticker_list() 오류
#for ticker in stock.get_stock_ticker_list():
#    df = stock.get_market_ohlcv_by_date("20211001", "20211101", ticker)
#    print(df.head())
#    time.sleep(2)

# df = stock.get_market_ohlcv_by_date("20150720", "20150810", "005930")
# if df.empty :
#    print("error")
# else:
#    print(df)

# df = stock.get_market_ohlcv_by_date("20150720", "20150810", "005930", adjusted=False)
# print(df.head(3))

#df = stock.get_market_ohlcv_by_ticker("20211101", market="ALL")
#print(df.head(3))

#df = stock.get_market_ohlcv_by_ticker("20200831", market="KOSPI")
#df = stock.get_market_ohlcv_by_ticker("20200831", market="KOSDAQ")
#df = stock.get_market_ohlcv_by_ticker("20200831", market="KONEX")

