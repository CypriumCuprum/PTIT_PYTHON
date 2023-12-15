for _ in range(int(input())):
    s = input()
    ss = 0
    rs = ""
    li = []
    for i in range(len(s)):
        if str.isdigit(s[i]):
            ss += (ord(s[i]) - 48)
        else:
            li.append(s[i])
    li = sorted(li)
    print("".join(li) + str(ss))
