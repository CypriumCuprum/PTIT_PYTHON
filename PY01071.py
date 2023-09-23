s = input()
ok = True
cnt_dot = 0
for i in range(len(s)):
    if s[i] == '.':
        cnt_dot += 1
if cnt_dot > 1:
    ok = False
if ok:
    if s[-3:].lower() != '.py':
        ok = False
if ok:
    print("yes")
else:
    print("no")