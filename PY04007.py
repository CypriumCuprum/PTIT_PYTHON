class Matrix:
    def __init__(self, n, m, matrix):
        self.n = n
        self.m = m
        self.matrix = matrix

    def cv(self):
        rs = [[0 for i in range(self.n)] for j in range(self.m)]
        for i in range(self.n):
            for j in range(self.m):
                rs[j][i] = self.matrix[i][j]
        return rs

    def pro(self, ma):
        rs = [[0 for i in range(self.n)] for j in range(self.n)]
        for i in range(self.n):
            for j in range(self.n):
                for l in range(self.m):
                    rs[i][j] += self.matrix[i][l] * ma[l][j]
        return rs


e = []
while True:
    try:
        e.extend(map(int, input().split()))
    except:
        break
I = 1
for _ in range(e[0]):
    n, m = e[I], e[I + 1]
    I += 2
    matrix = []
    for i in range(n):
        mms = []
        for j in range(m):
            mms.append(e[I])
            I += 1
        matrix.append(mms)
    mm = Matrix(n, m, matrix)
    mcv = mm.cv()
    s = mm.pro(mcv)
    for i in range(n):
        for j in range(n):
            print(s[i][j], end=" ")
        print()
