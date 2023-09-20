import math

for _ in range(int(input())):
    s = input()
    tong = 0
    rs = "YES"
    for i in range(len(s)):
        tong += int(s[i])
        if i%2 == 0 and int(s[i])%2==1:
            rs = "NO"
        if i%2 == 1 and int(s[i])%2==0:
            rs = "NO"
    if rs == "YES":
        if tong == 0 or tong == 1:
            rs = "NO"
        for i in range(2, round(math.sqrt(tong))+1):
            if tong%i == 0:
                rs = "NO"
                break

    print(rs)
