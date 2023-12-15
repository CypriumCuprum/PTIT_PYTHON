snt = [0] * 1000001
snt[0] = snt[1] = 1
for i in range(2, 1000):
    if snt[i] == 0:
        for j in range(i * i, 1000001, i):
            snt[j] = 1

n, m = map(int, input().split())
matrix = []
for _ in range(n):
    matrix.append(list(map(int, input().split())))
for i in range(n):
    for j in range(m):
        if snt[matrix[i][j]] == 0:
            print("1", end=" ")
        else:
            print("0", end=" ")
    print()
