import datetime

f = open('time.txt', mode='a', encoding='utf-8')

now = datetime.datetime.now()
print(now)

f.write(str(now)+"\n")

f.close()

r = open('time.txt', mode='r', encoding='utf-8')
#line = r.read()
#r.seek(0)
#line = r.readline(1)
line = r.readlines()
#line = r.read(50)
print(str(line) + 'read')

r.close()
#import time

#now = time.localtime()
#print("%04d/%02d/%02d %02d:%02d:%02d" % (now.tm_year, now.tm_mon, now.tm_mday, now.tm_hour, now.tm_min, now.tm_sec))


