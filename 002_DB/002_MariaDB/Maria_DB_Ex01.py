# 파이썬에서 MariaDB에서 sql문으로 MariaDB생성
import pymysql

# 전역변수 선언부
conn = None
cur = None

sql=""

# 메인 코드
conn = pymysql.connect(
    host='127.0.0.1',
    user='root',
    password='password',
    db='test',
    charset='utf8'
)  # 접속번호
cur = conn.cursor()  # 커서생성

sql ="CREATE TABLE IF NOT EXISTS users(deptname char(50), userName char(50), id int, salary float)"  # 실행할 sql문
cur.execute(sql)  # 커서로 sql문 실행

conn.commit()  # 저장

conn.close()  # 종료


