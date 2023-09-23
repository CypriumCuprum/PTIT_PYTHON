import math


def check_snt(n):
    if n == 0 or n == 1:
        return False
    for i in range(2, round(math.sqrt(n)+1)):
        if n % i == 0:
            return False
    return True


for _ in range(int(input())):
    s = input()
    ok = True
    if not check_snt(len(s)):
        ok = False
    cnt_snt = 0
    if ok:
        for i in range(len(s)):
            if check_snt(int(s[i])):
                cnt_snt += 1
        if cnt_snt*2 <= len(s):
            ok = False
    if ok:
        print("YES")
    else:
        print("NO")
