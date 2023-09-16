for _ in range(int(input())):
    s = input()
    a = int(s[-4:])
    ok = True
    for i in range(2, a):
        if a % i == 0:
            ok = False
            break
    if a == 1 or a == 0:
        ok = False
    if ok:
        print("YES")
    else:
        print("NO")