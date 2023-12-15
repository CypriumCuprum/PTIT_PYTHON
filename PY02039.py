n = int(input())
matrix = []
s = 0
for i in range(n):
    matrix.append(list(map(int, input().split())))
    s += sum(matrix[i])
k = int(input())
up = 0
diagonal = 0
for i in range(n):
    for j in range(n):
        if i < j:
            up += matrix[i][j]
        if i == j:
            diagonal += matrix[i][j]
low = s - diagonal - up

rs = abs(up - low)
rstr = "YES"
if rs > k:
    rstr = "NO"
print(rstr)
print(rs)
