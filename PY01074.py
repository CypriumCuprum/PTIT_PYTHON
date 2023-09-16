import time
start = time.time()
dic = {i:0 for i in range(5, 2000006, 2)}
dic[0] = 0
dic[1] = 0
for i in range(3, 2000006, 2):
    if dic[i] == 0:
        for j in range(3 * i, 2000006, 2*i):
            dic[j] = i

for i in range(3, 2000006, 2):
    if dic[i] == 0:
        dic[i] = i
    else:
        dic[i] = dic[dic[i]] + dic[int(i/dic[i])]

rs = 0
from sys import stdin
import random
for _ in range(1000000):
    n = random.randint(2, 1000005)
    while n % 2 == 0:
        rs += 2
        n = int(n/2)
    rs += dic[n]

print(rs)
print(time.time() - start)
