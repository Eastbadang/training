import time
cnt = 0
start = time.time()

for i in range(int(1e8)):
    cnt += i

print(time.time() - start)