for _ in range(int(input())):
    mp = [0] * 1001
    n = int(input())
    for i in range(n):
        t = int(input())
        mp[t] += 1
    rs = 0
    mp[0] = 0
    for i in range(1001):
        if mp[i] > mp[rs]:
            rs = i
        elif mp[i] == mp[rs]:
            if i < rs:
                rs = i
    print(rs)
