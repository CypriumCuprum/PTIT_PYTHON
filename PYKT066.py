import math
MAX = 10000

def process(divk1,k):
    divk2 = divk1[:]
    t = len(divk2)
    dp = [[0 for i in range(t)] for _ in range(t)]
    for i in range(t):
        dp[i][i] = divk2[i]
    rs = MAX
    for i in range(t):
        for j in range(0, i):
            dp[j][i] = math.gcd(dp[j][i-1], divk2[i])
            if dp[j][i] == k:
                rs = min(rs, i-j+1)
    return rs


for _ in range(int(input())):
    n, k1 = input().split()
    n = int(n)
    k = int(k1)
    li = input().split()

    """
    rs = MAX
    divk = []
    for i in li:
        if int(i) == k:
            rs = 1
            break
        if int(i) % k == 0:
            divk.append(int(i))
        else:
            if len(divk) >= 2:
                rs = min((process(divk, k), rs))
            divk = []
    """
    rs = MAX
    divk2 = []
    for i in li:
        if int(i) == k:
            rs = 1
        divk2.append(int(i))

    dp = [[0 for i in range(n)] for _ in range(n)]
    for i in range(n):
        dp[i][i] = divk2[i]

    for i in range(n):
        for j in range(0, i):
            dp[j][i] = math.gcd(dp[j][i - 1], divk2[i])
            if dp[j][i] == k:
                rs = min(rs, i - j + 1)
    if rs == MAX:
        print(-1)
    else:
        print(rs)