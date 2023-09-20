import math

for _ in range(int(input())):
    s = input()
    tich = 1
    for i in range(len(s)):
        if s[i] != '0':
            tich *= int(s[i])

    print(tich)
