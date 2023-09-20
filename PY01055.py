for _ in range(int(input())):
    s = input()
    rs = "YES"
    if s[0] == s[1] or len(s)%2 == 0:
        rs = "NO"
    for i in range(2, len(s), 2):
        if s[i] != s[i-2]:
            rs = "NO"
            break
    print(rs)