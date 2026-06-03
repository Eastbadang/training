# Excel 연동을 위한 Python package
# xlwt, xlrd, xlsxwriter, OpenPyxl
# xlwt/xlrd : excel 97, 2000, xp, 2003 포맷만 지원
# OpenPyxl : excel 2010 이상 포맷 지원

# 처음 패키지 설치 : pip install OpenPyxl

# 라이브러리 요청
import openpyxl

# wb=openpyxl.Workbook()
# sheet=wb.active
# sheet['A1']='HELLO WORLD'
# wb.save('HELLOWORLD.XLSX')

# 엑셀파일 열기
wb=openpyxl.load_workbook('stats_104102.xlsx')

#맨 앞의 시트 추출
sheet=wb.worksheets[0]

#시트의 각 행을 순서대로 추출하기
data=[]

for row in sheet.rows:
    data.append([row[0].value, row[10].value])

# 필요없는 줄(헤더, 연도, 계) 제거
del data[0]
del data[1]
del data[2]

# 데이터를 인구 순서로 정렬
data = sorted(data, key=lambda x:x[1])

# 하위 5위 출력
for i, a in enumerate(data):
    if (i >=5): break
    print(i+1,a[0], int(a[1]))

print("OK")


