a, k, n = input().split()
a = int(a)
k = int(k)
n = int(n)
m = int(a/k)
m += 1
b = m*k - a
ok = False
while b+a <= n:
    print(b, end=" ")
    b += k
    ok = True
if not ok:
    print(-1)