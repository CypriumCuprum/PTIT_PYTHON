while True:
    mi = 10 ** 200
    ma = -10 ** 200
    t = int(input())
    if t == 0:
        break
    for i in range(t):
        n = int(input())
        if n < mi:
            mi = n
        if n > ma:
            ma = n
    if mi != ma:
        print(mi, ma)
    else:
        print("BANG NHAU")
