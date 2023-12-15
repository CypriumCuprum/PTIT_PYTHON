import math

m, n = map(int, input().split())
print(str(int(m / math.gcd(m, n))) + "/" + str(int(n / math.gcd(m, n))))
