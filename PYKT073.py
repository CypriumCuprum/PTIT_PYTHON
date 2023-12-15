li = []
cnt = 0
n = int(input())
for i in range(n):
    s = input().split()
    li.append(len(s) % 2)
i = 0
rs = []
while i < len(li):
    if li[i] == 0:
        while i < len(li) and li[i] == 0:
            i += 1
        rs.append(1)
    else:
        i += 4
        rs.append(2)
print(len(rs))
for j in rs:
    print(j)
