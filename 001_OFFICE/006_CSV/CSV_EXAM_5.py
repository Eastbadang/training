import pandas as pd

xlsx = pd.read_excel('./sample.xlsx')
print(xlsx.head())
print()
print(xlsx.tail())
print()
print(xlsx.shape)
print(xlsx)

xlsx = pd.read_excel('./sample.xlsx', header=10)
print(xlsx)

# Pandas로 엑셀, csv 쓰기
xlsx.to_excel('./pandas_result.xlsx',index=False) # index : 첫 열에 숫자 붙여주기
xlsx.to_csv('./pandas_csv.csv',index=False)

