for _ in range(int(input())):
    a = input()
    b = input()
    rs = 0
    run = 0
    while run < len(a):
        if run+len(b) <= len(a) and a[run:run+len(b)] == b:
            rs += 1
            run += (len(b)-1)
        run += 1
    print(rs)
