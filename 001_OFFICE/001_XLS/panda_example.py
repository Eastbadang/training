import pandas as pd

# 파일 읽기
sales = pd.read_excel('SupermarketSales.xlsx')
#type(sales)
#print(sales)

# 데이터 정렬하기
#sales = sales.sort_values('지점')
#print(sales)

# 내림차순 정렬하기
#sales = sales.sort_values('지점', ascending=False)
#print(sales)

# 여러 개의 열을 기준으로 정렬하기
#sales = sales.sort_values(by=['지점', '고객타입'], ascending=[True, False])
#print(sales)

# 데이터 필터링 하기
# 지점 컬럼의 값이 A와 같은지 비교
#condition_A = (sales['지점'] == 'A')
# 데이터프레임에서 위의 조건을 만족하는 데이터만 필터링함
#sales_from_A = sales[condition_A]
#print(sales_from_A)

#condition_member = (sales['고객타입']=='회원')
#sales_member = sales[condition_member]
#print(sales_member)

#condition_female = (sales['성별']=='여성')
#sales_female = sales[condition_female]
#print(sales_female)

# 다수 조건 동시 만족하는 데이터 필터링
#sales_all_condition = sales[condition_A & condition_member & condition_female]
#print(sales_all_condition)

# 매출 원가율 계산
#sales['매출원가율'] = sales['매출원가'] / sales['매출액']
#print(sales)

# 사칙연산하기
# 덧셈
#sales['새컬럼명'] = sales['기존컬럼1'] + sales['기존컬럼2']
# 뺄셈
#sales['새컬럼명'] = sales['기존컬럼1'] - sales['기존컬럼2']
# 나눗셈
#sales['새컬럼명'] = sales['기존컬럼1'] / sales['기존컬럼2']
# 곱셉
#sales['새컬럼명'] = sales['기존컬럼1'] * sales['기존컬럼2']

# 복잡한 연산도 가능합니다
#sales['새컬럼명'] = (sales['기존컬럼1'] + sales['기존컬럼2']) / sales['기존컬럼3']


# 새로운 엑셀 파일을 불러옵니다.
# PrdManager.xlsx 파일을 읽어와 그 결과를 prd_manager라는 이름의 변수에 저장합니다.
#prd_manager = pd.read_excel('PrdManager.xlsx')
# 결과를 출력합니다.
#print(prd_manager)

# 데이터를 하나로 합치기
#sales = pd.merge(sales, prd_manager, how='left', on='제품군')
#print(sales)

# 판다스 피벗 테이블 만들기
#table = pd.pivot_table(sales, index='제품군', columns='날짜', values='매출액', aggfunc='sum')
#print(table)

# 월별 집계하기
sales['월'] = sales['날짜'].dt.strftime('%m')
#print(sales)
table = pd.pivot_table(sales, index='제품군', columns='월', values='매출액', aggfunc='sum')
print(table)