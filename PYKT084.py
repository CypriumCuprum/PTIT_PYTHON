n = int(input())
rs = []
run = 1
while run <= n:
    cnt = 0
    s = input()
    run += 1
    while run <= n:
        t = input()
        run += 1
        if t == "":
            break
        cnt += 1
    rs.append("{}: {}".format(s, str(cnt)))
for i in rs:
    print(i)
