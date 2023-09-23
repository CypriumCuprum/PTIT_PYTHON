n = int(input())
li = input().split()
rs = 0
for i in range(n):
    for j in range(i+1,n):
        if int(li[i]) > int(li[j]):
            rs += 1
print(rs)