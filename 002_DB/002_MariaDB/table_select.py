import pymysql

# 전역변수 선언부
conn = None
cur = None

sql=""

conn = pymysql.connect(
    host='127.0.0.1',
    user='root',
    password='password',
    db='mydatabase',
    charset='utf8'
)  # 접속번호

cur = conn.cursor()

cur.execute("SELECT * FROM customers")

myresult = cur.fetchall()

for x in myresult:
    print(x)

conn.commit()  # 저장

conn.close()  # 종료
