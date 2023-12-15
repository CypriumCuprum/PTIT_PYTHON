full = ""
while True:
    try:
        s = input()
        ok = ""
        for i in range(len(s)):
            ok += s[i]
            if s[i] == '.' or s[i] == '!' or s[i] == '?':
                li = ok.split()
                rs = (" ".join(li)).capitalize()
                dau = rs[-1]
                rs = rs[:-1].strip() + dau
                print(rs.capitalize())

                ok = ""
        if ok != "":
            li = ok.split()
            rs = (" ".join(li)).capitalize()
            dau = "."
            rs = rs.strip() + dau
            print(rs.capitalize())

    except EOFError:
        break
