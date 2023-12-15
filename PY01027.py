s = input()
ok = True
for i in range(len(s)):
    if s[i] != '6' and s[i] != '8':
        ok = False
        break
if s[0] == '8':
    ok = False
if ok:
    dp = [False] * (len(s) + 1)
    dp[0] = True
    if len(s) >= 2 and s[:2] == '68':
        dp[1] = True
    if len(s) >= 3 and s[:3] == '688':
        dp[2] = True
    for i in range(0, len(s)):
        if dp[i] == False:
            ok = False
            break
        j1 = i + 1
        j2 = i + 2
        j3 = i + 3
        if j1 < len(s) and s[i + 1:j1 + 1] == '6':
            dp[j1] = dp[i]
        if j2 < len(s) and s[i + 1:j2 + 1] == '68':
            dp[j2] = dp[i]
        if j3 < len(s) and s[i + 1:j3 + 1] == '688':
            dp[j3] = dp[i]
if ok:
    print("YES")
else:
    print("NO")
