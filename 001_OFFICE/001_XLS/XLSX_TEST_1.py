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

#활성화 시트 추출
sheet=wb.active

# 서울 제외한 인구 구해서 쓰기
for i in range(0, 10):
    total=int(sheet[str(chr(i+66))+"3"].value)
    seoul=int(sheet[str(chr(i+66))+"4"].value)
    output = total - seoul
    print("서울 제외 인구 =", output)

    # 쓰기
    sheet[str(chr(i+66))+"21"]=output
    cell=sheet[str(chr(i+66))+"21"]

    # 폰트와 색상 변경
    cell.font=openpyxl.styles.Font(size=14, color="FF0000")
    cell.number_format=cell.number_format

# 엑셀파일 저장
filename="population.xlsx"
wb.save(filename)
print("OK")

