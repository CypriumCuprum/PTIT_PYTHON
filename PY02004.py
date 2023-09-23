n = int(input())
li = input().split()
rs = 0
for i in range(1,n):
    if li[i] != li[i-1]:
        rs += 1

print(rs)