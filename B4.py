n, m, x = map(int, input().split())
li = [[] for _ in range(n+1)]

for _ in range(m):
    a,b = map(int, input().split())
    li[a].append(b)
    li[b].append(a)

vi, q = [0]*(n+1), [x]
vi[x] = 1
while len(q)>0:
    u = q.pop()
    for i in li[u]:
        if vi[i] == 0:
            q.append(i)
            vi[i] = 1
check = True
for i in range(1,n+1):
    if vi[i] == 0:
        check = False
        print(i)
if check:
    print(0)