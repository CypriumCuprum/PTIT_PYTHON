for _ in range(int(input())):
    n = int(input())
    n *= 2
    rs = 0
    for b in range(1, n):
        m = n
        m -= b * (b + 1)
        if m <= 0:
            break
        if m % (2 * (b + 1)) == 0:
            rs += 1
    print(rs)
