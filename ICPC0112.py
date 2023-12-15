snt = [0] * 1000001
snt[0] = snt[1] = 1
for i in range(2, 1000):
    if snt[i] == 0:
        for j in range(i * i, 1000001, i):
            snt[j] = 1

for _ in range(int(input())):
    N = int(input())
    ans = 0
    for i in range(3, N, 2):
        if i + 6 >= N:
            break
        if snt[i] == 0 and snt[i + 6] == 0:
            if snt[i + 2] == 0:
                ans += 1
            if snt[i + 4] == 0:
                ans += 1
    print(ans)
