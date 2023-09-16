for _ in range(int(input())):
    s = input()
    cnt_snt = 0
    k = len(s)
    ok = 0
    for i in range(2,k):
        if k % i == 0:
            ok = -1
            break
    if k == 1:
        ok = -1
    snt = [2, 3, 5, 7]
    for i in range(len(s)):
        if int(s[i]) in snt:
            cnt_snt += 1
    if cnt_snt*2 <= len(s):
        ok = -1
    if ok == 0:
        print("YES")
    else:
        print("NO")
