import re

dic = {}
t, k = map(int, input().split())
for _ in range(t):
    arr = re.split("[^a-z0-9]", input().lower())
    for i in arr:
        if i != "":
            if i in dic:
                dic[i] += 1
            else:
                dic[i] = 1

rs = []
for key, value in dic.items():
    rs.append((key, value))

rs.sort(key=lambda x: (-x[1], x[0]))
for i in rs:
    if i[1] >= k:
        print(i[0] + " " + str(i[1]))
