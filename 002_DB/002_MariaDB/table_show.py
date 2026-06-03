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
    db='mydatabase',
    charset='utf8'
)  # 접속번호
cur = conn.cursor()  # 커서생성

cur.execute("SHOW TABLES")

for x in cur:
    print(x)
