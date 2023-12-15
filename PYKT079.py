for _ in range(int(input())):
    n = int(input())
    li = list(set(list(map(int, input().split()))))
    a = max(li)
    b = min(li)
    print(a - b + 1 - len(li))
