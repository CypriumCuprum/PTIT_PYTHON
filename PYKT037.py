base = []
for i in range(0, 10):
    base.append(str(i))
for i in range(65, 65 + 26):
    base.append(chr(i));


# print(base)


def change(N, b):
    li = []
    while N > 0:
        li.append(base[N % b])
        N //= b
    li = li[::-1]
    print(''.join(li))


for _ in range(int(input())):
    N, b = map(int, input().split())
    change(N, b)
