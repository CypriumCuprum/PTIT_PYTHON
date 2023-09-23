import math


def check_snt(n):
    if n == 0 or n == 1:
        return False
    for i in range(2,round(math.sqrt(n))+1):
        if n%i == 0:
            return False
    return True


for _ in range(int(input())):
    s = input()
    ok = True
    for i in range(len(s)):
        if check_snt(i) and check_snt(int(s[i])) == False:
            ok = False
            break
        if check_snt(i) == False and check_snt(int(s[i])):
            ok = False
            break
    if ok:
        print("YES")
    else:
        print("NO")