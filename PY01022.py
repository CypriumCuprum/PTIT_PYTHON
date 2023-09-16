s = input()

rs = 0
while len(s) > 1:
    tong = 0
    for i in range(len(s)):
        tong += (ord(s[i]) - ord('0'))
    s = str(tong)
    rs += 1
print(rs)