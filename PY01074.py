import array as arr

li = arr.array('i', [0] * 2000001)
li[0] = li[1] = 0
for i in range(2, 1415):
    if li[i] == 0:
        for j in range(2 * i, 2000001, i):
            li[j] = i

for i in range(2, 2000001):
    if li[i] == 0:
        li[i] = i
    else:
        li[i] = li[li[i]] + li[i // li[i]]

rs = 0
from sys import stdin

for _ in range(int(stdin.readline())):
    rs += li[int(stdin.readline())]
print(rs)