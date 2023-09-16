s = input()
rs = ""
run = 0
for i in range(len(s)-1, -1,-1):
    if run == 3:
        rs = ","+rs
        run = 1
    else:
        run += 1
    rs = s[i]+rs
print(rs)
