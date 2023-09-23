fibo = [0 for _ in range(93)]
fibo[1] = 1
for i in range(2, 93):
    fibo[i] = fibo[i-1] + fibo[i-2]


for _ in range(int(input())):
    inn = input().split()
    start = int(inn[0])
    stop = int(inn[1])
    for i in range(start, stop+1):
        print(fibo[i], end=" ")
    print()