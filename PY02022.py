snt = [0] * 1000001
snt[0] = snt[1] = 0
for i in range(2, 1000):
    if snt[i] == 0:
        for j in range(i * i, 1000001, i):
            snt[j] = 1
n = int(input())
li = list(map(int, input().split()))
# li = sorted(li)
mp = {}
for i in li:
    if snt[i] == 0:
        if i not in mp:
            mp[i] = 1
        else:
            mp[i] += 1
for key, val in mp.items():
    print(key, val)
