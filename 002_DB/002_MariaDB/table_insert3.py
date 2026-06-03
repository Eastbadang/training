# db_create2.py 이후
# table_create2.py 이후

import pymysql

conn = pymysql.connect(
    host='127.0.0.1',
    user='root',
    password='password',
    db='testdb',
    charset='utf8'
)  # 접속번호

sql = "INSERT INTO user (name, email) VALUES (%s, %s)"

with conn:
    with conn.cursor() as cur:
        cur.execute(sql, ('Jaehee', 'jaehee@example.com'))
        cur.execute(sql, ('jeongeun', 'jeongeun@example.com'))
        conn.commit()  # 저장
