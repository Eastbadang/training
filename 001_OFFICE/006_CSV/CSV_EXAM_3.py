
import pandas as pd

output = pd.read_csv("./output.csv")

# output 데이터 살펴보기
output.describe(include="all")
print(output)