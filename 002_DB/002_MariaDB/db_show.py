import pymysql

# 전역변수 선언부
conn = None
cur = None

sql=""

conn = pymysql.connect(
    host='127.0.0.1',
    user='root',
    password='password',
    charset='utf8'
)  # 접속번호

cur = conn.cursor()

cur.execute("SHOW DATABASES")

for x in cur:
    print(x)

conn.commit()  # 저장

conn.close()  # 종료
