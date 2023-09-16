for _ in range(int(input())):
    s = input()
    ok = True
    for i in range(2, len(s), 2):
        if s[i] != s[i-2]:
            ok = False
    for i in range(3, len(s), 2):
        if s[i] != s[i-2]:
            ok = False
    if s[0] == s[1]:
        ok = False
    if ok:
        print("YES")
    else:
        print("NO")