for _ in range(int(input())):
    inn = input().split()
    n = int(inn[0])
    d = int(inn[1])
    li = input().split()
    rs = li[d:] + li[:d]
    for i in rs:
        print(i, end=" ")
    print()