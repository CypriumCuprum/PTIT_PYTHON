"""
(a^0+a^1 a^2 ...a^n-1 )(a-1) = a^n  - 1
0 -> 1
1 -> 2
2 -> 4
"""


def convert(s):
    rs = []
    while s > 0:
        rs.append(s % 2)
        s //= 2
    return rs[:]


MOD = 10 ** 9 + 7
for _ in range(int(input())):
    n, k = map(int, input().split())
    change = convert(k)
    rs = 0
    for i in range(len(change)):
        if change[i] == 1:
            rs += n ** i
            rs %= MOD
    print(rs)
