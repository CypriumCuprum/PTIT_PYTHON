import math

s = list(map(int, input().split()))

tu = int(s[0] * s[3] + s[1] * s[2])
mau = int(s[1] * s[3])
gg = math.gcd(tu, mau)
tu //= gg
mau //= gg
print(str(tu) + "/" + str(mau))
