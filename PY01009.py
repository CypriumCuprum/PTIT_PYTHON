s = input()
cnt_up = 0
cnt_low = 0
for i in range(len(s)):
    if s[i] >= 'a' and s[i] <= 'z':
        cnt_low += 1
    elif s[i] >= 'A' and s[i] <= 'Z':
        cnt_up += 1

if cnt_up > cnt_low:
    print(s.upper())
else:
    print(s.lower())