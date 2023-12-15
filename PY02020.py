n = int(input())
li = list(map(float, input().split()))

li = sorted(li)
sum = 0
cnt = 0
for i in li:
    if i != li[0] and i != li[n - 1]:
        sum += i
        cnt += 1
print("%.2f" % (sum / cnt))
