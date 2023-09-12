P = "ABCDEFGHIJKLMNOPQRSTUVWXYZ_."

while True:
    s1 = input()
    if s1 == '0':
        break

    k, s = s1.split()
    k = int(k)
    rs = ""
    for i in range(len(s)):
        pos = 0
        for j in range(len(P)):
            if s[i] == P[j]:
                pos = j
                break
        rs += P[(pos+k) % 28]
    print(rs[::-1])
