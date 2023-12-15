for _ in range(int(input())):
    s = input().split()
    rs = s[0]
    if len(rs) > 100:
        print("")
        continue
    for i in range(1, len(s)):
        if len(rs + " " + s[i]) > 100:
            break
        rs = rs + " " + s[i]
    print(rs)
