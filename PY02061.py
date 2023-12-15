def cn(ma, kernel):
    rs = 0
    for i in range(0, len(ma) - 2):
        for j in range(0, len(ma[0]) - 2):
            ad = 0
            for h in range(0, 3):
                for k in range(0, 3):
                    ad += (kernel[h][k] * ma[i + h][j + k])
            rs += ad
    return rs


for _ in range(int(input())):
    n, m = map(int, input().split())
    matrix = []
    kernel = []
    for i in range(n):
        matrix.append(list(map(int, input().split())))
    for i in range(3):
        kernel.append(list(map(int, input().split())))
    rs = cn(matrix, kernel)
    print(rs)
