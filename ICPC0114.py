import math

digitsnt = ['2', '3', '5', '7']


def checksnt(s):
    if s < 2:
        return False
    if s == 2:
        return True
    for i in range(3, int(math.sqrt(s) + 1), 2):
        if s % i == 0:
            return False
    return True


def checkdigit(s):
    su = 0
    for i in range(len(s)):
        su += int(s[i])
        if s[i] not in digitsnt:
            return False
    if checksnt(su) == False:
        return False
    return True


for _ in range(int(input())):
    n = input().strip()
    if checkdigit(n) and checksnt(int(n)) == True and checksnt(int(n[::-1])) == True:
        print("Yes")
    else:
        print("No")
