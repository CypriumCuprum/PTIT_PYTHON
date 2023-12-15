def rotate_step(ss):
    rs = 0
    for i in range(len(ss)):
        rs += (ord(ss[i]) - ord('A'))
    return rs % 26


def rotate(ss):
    rs = ""
    step = rotate_step(ss)
    for i in range(len(ss)):
        rs += chr(ord('A') + (ord(ss[i]) + step - ord('A')) % 26)
    return rs


for _ in range(int(input())):
    s = input().strip()
    half1 = ""
    half2 = ""
    for i in range(len(s) // 2):
        half1 += s[i]
    for i in range(len(s) // 2, len(s)):
        half2 += s[i]
    half2 = rotate(half2)
    half1 = rotate(half1)
    rs = ""
    for i in range(len(half1)):
        rs += chr(ord('A') + (ord(half1[i]) + ord(half2[i]) - 2 * ord('A')) % 26)
    print(rs)
