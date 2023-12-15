def tinhgom(s):
    run = 2 ** (len(s) - 1)
    rs = 0
    for i in range(len(s)):
        if s[i] == '1':
            rs += run
        run //= 2
    if rs >= 10:
        ans = chr(rs + 65 - 10)
    else:
        ans = str(rs)
    return ans


def change(gom, s):
    rs = ""
    while len(s) % gom != 0:
        s = '0' + s
    for i in range(0, len(s), gom):
        rs += tinhgom(s[i:i + gom])
    return rs


f = open("DATA.in", 'r')
for _ in range(int(f.readline().strip())):
    n = int(f.readline().strip())
    s = f.readline().strip()
    gom = 1
    while 2 ** gom < n:
        gom += 1
    print(change(gom, s))
f.close()
