for _ in range(int(input())):
    n = int(input())
    li = sorted(list(map(int, input().split())))
    rs = 0
    for i in range(n):
        l, r = i + 1, n - 1
        while l < r:
            s = li[l] + li[i] + li[r]
            if s == 0:
                rs += 1
                l += 1

            elif s > 0:
                r -= 1
            else:
                l += 1
    print(rs)
