fibo = [0,1,1]
for i in range(3, 94):
    fibo.append(fibo[i-1]+fibo[i-2])

for _ in range(int(input())):
    s = input().split()
    a = int(s[0])
    b = int(s[1])
    for i in range(a,b+1):
        print(fibo[i], end=" ")
    print()
