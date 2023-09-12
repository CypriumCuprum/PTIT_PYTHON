import math


def check(n):
    chec = 0
    for i in range(len(str(n))):
        chec += int(str(n)[i])
    if chec == 1:
        return False
    if chec == 2:
        return True
    for i in range(2, round(math.sqrt(chec))+1):
        if chec % i == 0:
            return False
    return True


for _ in range(int(input())):
    a, b = input().split()
    a = int(a)
    b = int(b)
    c = math.gcd(a, b)
    if check(c):
        print("YES")
    else:
        print("NO")
