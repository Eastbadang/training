import csv

f = open('D:\\WORKS\\PyCharmProjects\\001_TRAINING\\001_OFFICE\\006_CSV\\output.csv','r', encoding='utf-8')
rdr = csv.reader(f)

for line in rdr:
    print(line)
f.close()