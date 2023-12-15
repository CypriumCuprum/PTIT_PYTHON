import math

n = int(input())
li = list(map(int, input().split()))
li = sorted(li)
ans = []
for i in range(len(li)):
    for j in range(i + 1, len(li)):
        if math.gcd(li[i], li[j]) == 1:
            print(li[i], li[j])
