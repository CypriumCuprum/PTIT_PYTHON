for t in range(int(input())):
    print("Test {}: ".format(t + 1), end="")
    s1 = input()
    s2 = input()
    li1 = []
    li2 = []
    for i in range(len(s1)):
        li1.append(s1[i])
    for i in range(len(s2)):
        li2.append(s2[i])
    li1 = sorted(li1)
    li2 = sorted(li2)
    if li1 == li2:
        print("YES")
    else:
        print("NO")
