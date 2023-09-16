import math

l, r = input().split()
l = int(l)
r = int(r)


def printt(a, b, c):
    print(f"({a}, {b}, {c})")

for i in range(l, r+1):
    for j in range(i+1, r+1):
        for k in range(j+1, r+1):
            if math.gcd(i, j) == 1 and math.gcd(i, k) == 1 and math.gcd(j, k) == 1:
                printt(i, j, k)