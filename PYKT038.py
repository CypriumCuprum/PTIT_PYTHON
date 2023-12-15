def change(sub):
    rs = 0
    for i in range(len(sub)):
        if sub[i] == '1':
            rs += (1 << (2 - i))
    return rs


s = input()
while len(s) % 3 != 0:
    s = '0' + s
for i in range(0, len(s), 3):
    print(change(s[i:(i + 3)]), end="")
