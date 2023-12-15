def tongcs(n):
    rs = 0
    while n > 0:
        rs += (n % 10)
        n //= 10
    return rs


def com(a, b):
    if tongcs(a) == tongcs(b):
        return a < b
    return tongcs(a) < tongcs(b)


for _ in range(int(input())):
    n = int(input())
    li = list(map(int, input().split()))
    for i in range(len(li)):
        # print(tongcs(li[i]), li[i])
        for j in range(i + 1, len(li)):
            if not com(li[i], li[j]):
                c = li[i]
                li[i] = li[j]
                li[j] = c
    for i in li:
        print(i, end=" ")
    print()
