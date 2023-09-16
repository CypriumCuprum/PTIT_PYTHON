for _ in range(int(input())):
    s = input()
    ok = 0
    run = 1
    while run < len(s) and s[run] > s[run-1]:
        run += 1
    if run == 1 or run == len(s):
        print("NO")
        continue
    while run < len(s) and s[run] < s[run-1]:
        run += 1

    if run == len(s):
        print("YES")
    else:
        print("NO")


