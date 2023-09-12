for _ in range(int(input())):
    s = input()
    run = 0
    cnt = 0
    rs = ""
    while run < len(s):
        cnt = 1
        while run < len(s)-1 and s[run] == s[run+1]:
            cnt += 1
            run += 1
        rs = rs + str(cnt) + s[run]
        run += 1
    print(rs)