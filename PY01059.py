for _ in range(int(input())):
    s = input()
    tong = 0
    tich = 1
    ok = 0
    for i in range(0, len(s), 2):
        tong += int(s[i])
    for i in range(1, len(s), 2):
        if s[i] != '0':
            ok = 1
            tich *= int(s[i])
    if ok == 0:
        tich = 0
    print(str(tong) + " " + str(tich))
