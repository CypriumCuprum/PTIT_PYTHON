for _ in range(int(input())):
    s = input()
    s1 = input()
    if len(s1) > len(s):
        print("0")
        continue
    k = len(s1)
    rs = 0
    i = 0
    while i <= len(s) - k + 1:
        if s[i:i + k] == s1:
            rs += 1
            i += k
        i += 1

    print(rs)
