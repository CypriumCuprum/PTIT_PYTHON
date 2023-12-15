dau = ['/', '+', '-', "*"]
s = ""
rs = []


def check(ok):
    a = int(ok[:2])
    dau = ok[3]
    b = int(ok[5:7])
    c = int(ok[-2:])
    # print(a, dau, b, c)
    if dau == '+': return a + b == c
    if dau == '-': return a - b == c
    if dau == "*": return a * b == c
    if dau == '/': return a % b == 0 and a // b == c
    return False


def make(i, ok, s):
    if i >= len(s):
        if check(ok):
            # print(ok)
            rs.append(ok)
        return
    if s[i] != '?':
        ok += s[i]
        if len(rs) == 0:
            make(i + 1, ok, s)
    else:
        if i == 3:
            for j in dau:
                ok = ok[:i] + str(j)
                if len(rs) == 0:
                    make(i + 1, ok, s)
        else:
            for j in range(10):
                if (i == 0 or i == 5 or i == 10) and j == 0:
                    continue
                ok = ok[:i] + str(j)
                if len(rs) == 0:
                    make(i + 1, ok, s)


for _ in range(int(input())):
    s = input()
    rs = []
    make(0, "", s)
    if rs == []:
        print("WRONG PROBLEM!")
    else:
        print(rs[0])
