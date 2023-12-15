l1 = list(map(int, input().split()))
n = l1[0]
k = l1[1]
li = list(map(int, input().split()))

li.sort()
rs = 1
for i in range(1, len(li)):
    if li[i] - li[i - 1] > k:
        rs += 1
print(rs)
