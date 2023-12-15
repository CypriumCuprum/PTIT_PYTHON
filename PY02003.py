li = [0]
q = []
for x in range(60):
    for y in range(38):
        for z in range(26):
            if (2 ** x) * (3 ** y) * (5 ** z) <= 1e18:
                li.append((2 ** x) * (3 ** y) * (5 ** z))
li = sorted(li)


def binsearch(l, r, n):
    if l > r:
        return -1
    mid = int((l + r) / 2)
    if li[mid] == n:
        return mid
    if li[mid] > n:
        return binsearch(l, mid - 1, n)
    else:
        return binsearch(mid + 1, r, n)


for i in range(int(input())):
    n = int(input())
    rs = binsearch(1, len(li), n)
    if rs == -1:
        print("Not in sequence")
    else:
        print(rs)
