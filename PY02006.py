for _ in range(int(input())):
    n = int(input())
    a = input().split()
    b = input().split()
    for i in range(n):
        a[i] = int(a[i])
        b[i] = int(b[i])
    x = sorted(a)
    y = sorted(b)
    ok = True
    for i in range(n):
        if x[i] > y[i]:
            ok = False
            break
    if ok:
        print("YES")
    else:
        print("NO")
