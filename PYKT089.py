e = []
while True:
    try:
        e.extend(map(int, input().split()))
    except:
        break
n = e[0]
li = e[1:]
even = []
odd = []
poseven = []
posodd = []
for i in range(len(li)):
    if li[i] % 2 == 0:
        even.append(li[i])
        poseven.append(i)
    else:
        odd.append(li[i])
        posodd.append(i)
rs = [0] * n
even = sorted(even)
odd = sorted(odd)
odd = odd[::-1]
run = 0
for i in poseven:
    rs[i] = even[run]
    run += 1
run = 0
for i in posodd:
    rs[i] = odd[run]
    run += 1
for i in rs:
    print(i, end=" ")
