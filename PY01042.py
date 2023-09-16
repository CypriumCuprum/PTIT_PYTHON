for _ in range(int(input())):
    s = input()
    li = ['1', '2', '0']
    rs = "YES"
    for i in range(len(s)):
        if s[i] not in li:
            rs = "NO"
            break
    print(rs)