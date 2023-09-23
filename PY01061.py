import math


def check_snt(n):
    if n == 0 or n == 1:
        return False
    for i in range(2, round(math.sqrt(n))+1):
        if n % i == 0:
            return False
    return True


for _ in range(int(input())):
    s = input()
    while len(s) < 4:
        s = '0'+s
    check1 = s[-3:]
    check2 = s[:3]
    if check_snt(int(check1)) and check_snt(int(check2)):
        print("YES")
    else:
        print("NO")