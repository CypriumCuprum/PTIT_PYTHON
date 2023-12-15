from sys import stdin

n, k, tmp, a, b = 0, 0, 0, [], []


def check(gg):
    left, right = 0, n
    while left < right:
        mid = (left + right)>>1
        if a[mid]<gg: left = mid + 1
        else: right = mid
    return b[left-1] >= gg*(left+tmp)


for t in range(int(stdin.readline())):
    n, k = map(int, stdin.readline().split())
    a = sorted(map(int, stdin.readline().split()))
    b = a.copy()
    for i in range(1, n): b[i]+=b[i-1]
    if n < k:
        print(0)
        continue
    if n == k:
        print(a[0])
        continue
    tmp = k-n
    l, r = 0, sum(a)//k
    while l<r:
        mid = (l+r)>>1
        if check(mid): l = mid + 1
        else: r = mid
    if check(l): print(l)
    else: print(l-1)