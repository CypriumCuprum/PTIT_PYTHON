for _ in range(int(input())):
    s = input()
    tong = 0
    for i in range(len(s)):
        tong += int(s[i])
    if str(tong) == str(tong)[::-1] and len(str(tong)) > 1:
        print("YES")
    else:
        print("NO")