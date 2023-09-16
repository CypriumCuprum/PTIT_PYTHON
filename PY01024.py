def check_sum10(s):
    sum = 0
    for i in range(len(s)):
        sum += int(s[i])
    if sum % 10 == 0:
        return True
    return False


def check_diff_2(s):
    for i in range(1, len(s)):
        if abs(ord(s[i]) -ord(s[i-1])) != 2:
            return False
    return True

for _ in range(int(input())):
    n = input()
    if check_sum10(n) and check_diff_2(n):
        print("YES")
    else:
        print("NO")
