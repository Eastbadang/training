# 파이썬에서 저장된 데이터를 변수로 받아 출력하는 프로그램
import pymysql

# 전역변수 선언부
conn = None
cur = None

data1 = ""
data2 = ""
data3 = ""
data4 = ""

row = None  # 테이블의 행을 받아줌

# 메인 코드
conn = pymysql.connect(
    host='127.0.0.1',
    user='root',
    password='password',
    db='test',
    charset='utf8'
)  # 접속번호
cur = conn.cursor()  # 커서생성

cur.execute("SELECT * FROM users")  # sql 변수 없이 SQL문을 직접 입력 후 커서로 실행

print("부서명 이름 ID 월급여")
print("-----------------------")

while(True):  # 반복실행
    row = cur.fetchone()  # row에 커서(테이블 셀렉트)를 한줄 입력하고 다음 줄로 넘어감
    if row == None:  # row에 커서(테이블 셀렉트)를 한줄 입력하고 다음 줄로 넘어 감
        break;  # while문을 떠남'
    data1 = row[0]
    data2 = row[1]
    data3 = row[2]
    data4 = row[3]
    print("%s %s %d %f" % (data1, data2, data3, data4))

conn.close()  # 종료


