import math

for _ in range(int(input())):
    n, m, k = map(int, input().split())
    matrix = []
    matrix.append([0] * (m + 1))
    for i in range(n):
        matrix.append([0] + list(map(int, input().split())))
    prefixsum = [[0] * (m + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            prefixsum[i][j] = prefixsum[i - 1][j] + prefixsum[i][j - 1] - prefixsum[i - 1][j - 1] + matrix[i][j]
    rs = []
    for i in range(1, n + 2 - k):
        row = []
        for j in range(1, m + 2 - k):
            rs1 = prefixsum[i + k - 1][j + k - 1] + prefixsum[i - 1][j - 1] - prefixsum[i + k - 1][j - 1] - \
                  prefixsum[i - 1][j + k - 1]
            row.append(math.floor(rs1 / (k * k)))
        rs.append(row)
    for i in range(len(rs)):
        for j in range(len(rs[0])):
            print(rs[i][j], end=" ")
        print()
