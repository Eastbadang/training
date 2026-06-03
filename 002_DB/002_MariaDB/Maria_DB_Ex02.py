# 파이썬으로 입력받은 값들을 테이블의 데이터로 입력하는 프로그램
import pymysql

# 전역변수 선언부
conn = None
cur = None

data1 = ""
data2 = ""
data3 = ""
data4 = ""

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

while(True):  # break를 만날 때까지 계속 반복
    data1 = input("사용자 부서명을 입력하세요(엔터 클릭 시 종료) : ")  # data1변수에 부서명 입력받기
    if data1 == "":  # 만약 data1에 아무값도 입력받지 않는 다면
        break;  # break;로 while문을 떠남'
    data2 = input("사용자 이름을 입력하세요 : ")
    data3 = input("사용자 ID를 입력하세요 : ")
    data4 = input("사용자 월급을 입력하세요 : ")
    sql = "INSERT INTO users VALUES('" + data1 + "','" + data2 + "','" + data3 + "','" + data4 + ")"  # sql 변수에 INSERT SQL문 입력
    cur.execute(sql)  # 커서로 sql 실행

conn.commit()  # 저장

conn.close()  # 종료


