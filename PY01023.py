li = [0]*1005
li[0] = li[1] = 0
snt = []
for i in range(2, 1005):
    if li[i] == 0:
        snt.append(i)
        for j in range(2*i, 1005, i):
            li[j] = 1

for _ in range(int(input())):
    n = int(input())
    rs = "1"
    run = 0
    while snt[run]*snt[run] <= n:
        cnt = 0
        while n % snt[run] == 0:
            cnt += 1
            n = round(n/snt[run])
        if cnt >= 1:
            rs = rs + " * "+str(snt[run]) + "^" + str(cnt)
        run += 1
    if n != 1:
        rs = rs + " * " + str(n) + "^1"
    print(rs)
