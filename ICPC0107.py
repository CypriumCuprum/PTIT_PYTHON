def com(s1, s2, x, y):
    s1_new = ""
    s2_new = ""
    for i in s1:
        if i == y:
            i = x
        s1_new = s1_new + i
    for i in s2:
        if i == y:
            i = x
        s2_new = s2_new + i
    return str(int(s1_new) + int(s2_new))


for _ in range(int(input())):
    a, b = input().split()
    if a > b:
        c = a
        a = b
        b = c
    s = input().split()
    if len(s) == 1:
        s2 = input()
    else:
        s2 = s[1]
    s1 = s[0]

    rs = com(s1, s2, a, b) + " " + com(s1, s2, b, a)
    print(rs)
