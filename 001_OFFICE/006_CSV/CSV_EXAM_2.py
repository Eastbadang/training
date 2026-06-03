import csv

with open('D:\\WORKS\\PyCharmProjects\\001_TRAINING\\001_OFFICE\\006_CSV\\output.csv') as csvfile:
    rdr = csv.DictReader(csvfile)
    for i in rdr:
      print(i)