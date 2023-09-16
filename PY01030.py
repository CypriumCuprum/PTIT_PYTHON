n, k = input().split()
n = int(n)
k = int(k)
run = 2
uoc = []
while run*run <= n:
    ok = 0
    while n % run == 0:
        ok = 1
        n = round(n/run)
    if ok:
        uoc.append(run)
    run += 1
if n != 1:
    uoc.append(n)
rs = ""
choose = [0]*100000
for i in uoc:
    for j in range(2*i, 10**k, i):
        choose[j] = 1

for i in range(10**(k-1), 10**k):
    if choose[i] == 0:
        rs = rs + str(i) + " "

print(rs)