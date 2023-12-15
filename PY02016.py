for _ in range(int(input())):
    mp = {}
    n = int(input())
    li = list(map(int, input().split()))
    for i in range(n):
        if li[i] not in mp:
            mp[li[i]] = 1
        else:
            mp[li[i]] += 1
    rs = 0
    mp[0] = 0
    for key, val in mp.items():
        if val > mp[rs]:
            rs = key
        elif val == mp[rs]:
            if key < rs:
                rs = key
    if (mp[rs] > n / 2):
        print(rs)
    else:
        print("NO")
