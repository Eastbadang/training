# db_create2.py 이후
# table_create2.py 이후
# table_insert3.py 이후

import pymysql

conn = pymysql.connect(
    host='127.0.0.1',
    user='root',
    password='password',
    db='testdb',
    charset='utf8'
)  # 접속번호

sql = "SELECT * FROM user where name = %s"

with conn:
    with conn.cursor() as cur:
        cur.execute(sql, ('Jaehee'))
        result = cur.fetchall()
        for data in result:
            print(data)
