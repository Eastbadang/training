import csv

f = open('D:\\WORKS\\PyCharmProjects\\001_TRAINING\\001_OFFICE\\006_CSV\\output.csv', 'w', encoding = 'utf-8')
wr = csv.writer(f)
wr.writerow([1,"Alice", True])
wr.writerow([2,"Bob", False])
f.close()