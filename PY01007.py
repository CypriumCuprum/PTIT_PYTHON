for _ in range(int(input())):
    s = input().split()
    cnt = 0
    n = float(s[0])
    x = float(s[1])
    m = float(s[2])
    while n+x*n/100 < m:
        n = n+x*n/100
        cnt += 1
    print(cnt+1)