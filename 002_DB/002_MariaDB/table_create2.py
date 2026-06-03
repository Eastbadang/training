# db_create2.py 이후
import pymysql

# 전역변수 선언부
conn = None
cur = None

sql=""

conn = pymysql.connect(
    host='127.0.0.1',
    user='root',
    password='password',
    db='testdb',
    charset='utf8'
)  # 접속번호

cur = conn.cursor()

cur.execute("CREATE TABLE user(name VARCHAR(255), email VARCHAR(255))")

conn.commit()  # 저장

conn.close()  # 종료
