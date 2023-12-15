n = int(input())
matrix = []
for i in range(n):
    matrix.append(input())
rs = 0
for i in range(n):
    tinh = 0
    for j in range(n):
        if matrix[i][j] == 'C':
            tinh += 1
    rs += tinh * (tinh - 1) // 2
for j in range(n):
    tinh = 0
    for i in range(n):
        if matrix[i][j] == 'C':
            tinh += 1
    rs += tinh * (tinh - 1) // 2
print(rs)
