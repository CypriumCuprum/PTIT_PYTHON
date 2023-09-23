def check(s):
    if len(s) % 2 == 1:
        return False
    for i in range(round(len(s)/2)):
        if s[i] != s[len(s)-1-i] or s[i] == '1' or s[i] == '3' or s[i] == '7' or s[i] == '9' or s[i] == '5':
            return False
    return True


MAX = 1e6+5
run = 22

li = []
while run < MAX:
    if check(str(run)):
        li.append(run)
    run += 2

for _ in range(int(input())):
    n = int(input())
    rs = "22"
    r = 1
    while r < len(li) and li[r] < n:
        rs = rs + " " + str(li[r])
        r += 1
    print(rs)

