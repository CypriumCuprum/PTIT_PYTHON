ox = [-1, -1, -1, 0, 0, 1, 1, 1]
oy = [-1, 0, 1, -1, 1, -1, 0, 1]

m, n = map(int, input().split())
matrix = []
for i in range(m):
    matrix.append(list(map(int, input().split())))
mark = [[0] * n for i in range(m)]
rs = 0
for i in range(m):
    for j in range(n):
        if matrix[i][j] == -1:
            for l in range(8):
                newrow = i + ox[l]
                newcol = j + oy[l]
                if 0 <= newcol and newcol < n and newrow >= 0 and newrow < m and mark[newrow][newcol] == 0:
                    rs += matrix[newrow][newcol]
                    mark[newrow][newcol] = 1
print(rs)
