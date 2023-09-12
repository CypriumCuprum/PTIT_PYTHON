for _ in range(int(input())):
    s = input()
    ok = True
    for i in range(1, len(s)):
        if s[i] < s[i-1]:
            ok = False
            break
    if ok:
        print("YES")
    else:
        print("NO")