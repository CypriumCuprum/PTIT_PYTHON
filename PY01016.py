for _ in range(int(input())):
    s = input()
    rs = ""
    for i in range(0, len(s),2):
       for _ in range(0, int(s[i+1])):
           rs += s[i]
    print(rs)