import math

for _ in range(int(input())):
    s = input()
    n1 = int(s)
    n2 = int(s[::-1])
    if math.gcd(n1, n2) == 1:
        print("YES")
    else:
        print("NO")
