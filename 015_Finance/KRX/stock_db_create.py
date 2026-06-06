# https://youngwonhan-family.tistory.com/entry/Python-%EC%83%81%EC%9E%A5%EB%B2%95%EC%9D%B8-%EC%A2%85%EB%AA%A9%EC%BD%94%EB%93%9C-%EB%8D%B0%EC%9D%B4%ED%84%B0%EB%B2%A0%EC%9D%B4%EC%8A%A4-%EA%B5%AC%EC%B6%95-MariaDB-%EC%BB%A4%EB%84%A5%EC%85%98-%EC%A0%80%EC%9E%A5-%EC%A1%B0%ED%9A%8C
# https://sweetquant.tistory.com/295
# pip install mariadb

import mariadb

conn = mariadb.connect(
    user='root',
    password='password',
    database='stock_ex',
    host='localhost'
)  # 접속번호

cur = conn.cursor()

#CREATE TABLE DB_DTECH.STOCK_KRX
#(
#	STK_CD    VARCHAR(40)   NOT NULL COMMENT '종목코드'
#	,STK_NM   VARCHAR(200)  NOT NULL COMMENT '종목명'
#	,SEC_NM   VARCHAR(500)  NULL     COMMENT '업종(섹터명)'
#	,MAIN_PRD VARCHAR(1000) NULL     COMMENT '주요제품'
#	,PUB_DT   DATE          NULL     COMMENT '상장일자'
#	,EX_CD    VARCHAR(40)   NOT NULL COMMENT '거래소코드'
#	,FRST_INP_DTM DATETIME  NULL     COMMENT '최초입력일시'
#	,LAST_CHG_DTM DATETIME  NULL     COMMENT '최종변경일시'
#	,PRIMARY KEY (STK_CD)
#) COMMENT 'KRX종목마스터';

sql ="CREATE TABLE IF NOT EXISTS stock_krx(STK_CD VARCHAR(40) NULL COMMENT '종목코드', STK_NM VARCHAR(200)  NULL COMMENT '종목명') COMMENT 'KRX종목마스터';"  # 실행할 sql문
cur.execute(sql)  # 커서로 sql문 실행

cur.execute("SHOW DATABASES")

rows = cur.fetchall()
print(rows)

conn.commit()  # 저장

conn.close()  # 종료
