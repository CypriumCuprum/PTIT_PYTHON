s1 = sorted(list(set(input().lower().split())))
s2 = sorted(list(set(input().lower().split())))
print(" ".join(sorted(list(set(s1 + s2)))))
for i in s1:
    if i in s2:
        print(i, end=" ")
