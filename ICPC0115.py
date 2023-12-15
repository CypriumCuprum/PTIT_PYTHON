giaithua = [1]
for i in range(1, 10):
    giaithua.append(giaithua[i - 1] * i)


def check(s):
    ok = 0
    for i in range(len(s)):
        ok += giaithua[int(s[i])]
    if str(ok) == s:
        return True
    return False


for _ in range(int(input())):
    n = input()
    if check(n):
        print("Yes")
    else:
        print("No")
