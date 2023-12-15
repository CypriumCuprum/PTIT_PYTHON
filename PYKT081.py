for _ in range(int(input())):
    try:
        l = input()
        s = l.split(".")
        if len(s) != 4:
            print("NO")
            continue
        ok = True
        for i in range(len(s)):
            if int(s[i]) > 255 or int(s[i]) < 0:
                print("NO")
                ok = False
                break
        if ok:
            print("YES")
    except:
        print("NO")
