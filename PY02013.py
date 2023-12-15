while True:
    n = int(input())
    if n == 0:
        break
    rs = 1
    while n > 1:
        if n % 2 == 0:
            n /= 2
        else:
            n = n*3+1
        rs += 1
    print(rs)


