snt = [0] * 1000001
snt[0] = snt[1] = 1
for i in range(2, 1000):
    if snt[i] == 0:
        for j in range(i * i, 1000001, i):
            snt[j] = 1

for _ in range(int(input())):
    n = int(input())
    li = []
    for i in range(13, n, 2):
        l = int(str(i)[::-1])
        if l < n and i != l and snt[i] == 0 and snt[l] == 0:
            if str(i) not in li:
                li.append(str(i))
                li.append(str(l))
    print(" ".join(li))
