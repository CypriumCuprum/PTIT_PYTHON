def cnt(a, b):
    rs = -1
    a = str(a)
    b = str(b)
    for i in range(len(a)):
        s1 = a[:i]
        if s1 in b:
            s2 = a[i:] + s1
            if s2 == b:
                rs = max(rs, len(a) - i)
    return rs


n = int(input())
li = []
for _ in range(n):
    li.append(input().strip())
ok = True
dis = [[0] * n for _ in range(n)]
for i in range(len(li)):
    if ok:
        for j in range(i + 1, len(li)):
            if ok:
                dis[i][j] = cnt(li[i], li[j])
                if dis[i][j] == -1:
                    ok = False
                    break
                dis[j][i] = len(li[i]) - dis[i][j]
    else:
        break
if not ok:
    print("-1")
else:
    print(min(sum(dis[i]) for i in range(n)))
