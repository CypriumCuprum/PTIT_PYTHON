import math

def isPrime(n):
    if n < 2:
        return False
    for i in range (2, n):
        if n % i == 0:
            return False
    return True

li = [0]
run = 2
while(run < 10000):
    if isPrime(run):
        li.append(run)
    run += 1
# print(li)
n, x = list(map(int, input().split()))
for i in range(n+1):
    x += li[i]
    print(x, end=" ")

