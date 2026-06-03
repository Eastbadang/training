# https://sweetquant.tistory.com/295

import mariadb
import pandas as pd

url = 'https://kind.krx.co.kr/corpgeneral/corpList.do' # KRX의 종목리스트 URL
KD = pd.read_html(url+"?method=download&marketType=kosdaqMkt")[0] #코스닥
KP = pd.read_html(url+"?method=download&marketType=stockMkt")[0] #코스피

print(KD) # 코스닥 종목 리스트 출력
print(KP) # 코스피 종목 리스트 출력
print(KD.columns) #종목 리스트를 구성하는 컬럼 확인

conn = mariadb.connect(
    user='root',
    password='1945!Akfldk',
    database='stock_ex',
    host='localhost'
)  # 접속번호

cur = conn.cursor()

# # KOSDAQ 종목 입력(위에 내용과 동일)
for row in KD.itertuples():
    STK_CD = str(row.종목코드).zfill(6)
    STK_NM = str(row.회사명)
    SEC_NM = str(row.업종).replace("'", ",")
    MAIN_PRD = str(row.주요제품).replace("'", ",")
    PUB_DT = str(row.상장일)
    EX_CD = 'KD' # KOSDAQ

    sql = "INSERT INTO STOCK_EX.STOCK_KRX(STK_CD ,STK_NM ,SEC_NM ,MAIN_PRD ,PUB_DT ,EX_CD ,FRST_INP_DTM)"
    sql = sql + "VALUES("
    sql = sql + "'" + STK_CD + "'"
    sql = sql + ",'" + STK_NM + "'"
    sql = sql + ",'" + SEC_NM + "'"
    sql = sql + ",'" + MAIN_PRD + "'"
    sql = sql + ",DATE_FORMAT('" + PUB_DT + "','%Y-%m-%d')"
    sql = sql + ",'" + EX_CD + "'"
    sql = sql + ",NOW())"
    print(sql)
    cur.execute(sql)
    cur.execute('commit')

# KOSPI 종목 입력(위에 내용과 동일)
for row in KP.itertuples():
    STK_CD = str(row.종목코드).zfill(6)
    STK_NM = str(row.회사명)
    SEC_NM = str(row.업종).replace("'", ",")
    MAIN_PRD = str(row.주요제품).replace("'", ",")
    PUB_DT = str(row.상장일)
    EX_CD = 'KP' # KOSPI

    sql = "INSERT INTO STOCK_EX.STOCK_KRX(STK_CD ,STK_NM ,SEC_NM ,MAIN_PRD ,PUB_DT ,EX_CD ,FRST_INP_DTM)"
    sql = sql + "VALUES("
    sql = sql + "'" + STK_CD + "'"
    sql = sql + ",'" + STK_NM + "'"
    sql = sql + ",'" + SEC_NM + "'"
    sql = sql + ",'" + MAIN_PRD + "'"
    sql = sql + ",DATE_FORMAT('" + PUB_DT + "','%Y-%m-%d')"
    sql = sql + ",'" + EX_CD + "'"
    sql = sql + ",NOW())"
    print(sql)
    cur.execute(sql)
    cur.execute('commit')
