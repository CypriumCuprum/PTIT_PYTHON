for _ in range(int(input())):
    n = input()
    run = 0
    while run < 1000 and int(n)%7 != 0 and (int(n) + int(n[::-1])) % 7 != 0:
        n = str(int(n) + int(n[::-1]))
        run += 1
    if run == 1000:
        print(-1)
    elif int(n) % 7 == 0:
        print(n)
    else:
        print(str(int(n) + int(n[::-1])))
