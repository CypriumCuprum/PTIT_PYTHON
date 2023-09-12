for _ in range(int(input())):
    s = input()
    s1 = s[:2]
    s2 = s[len(s)-2:len(s)]
    print(s1)
    print(s2)
    if s1 == s2:
        print("YES")
    else:
        print("NO")