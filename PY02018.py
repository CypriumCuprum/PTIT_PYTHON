n = int(input())
li = list(map(int, input().split()))
li = sorted(li)
run = li[0]
ok = False
for i in range(len(li)):
    if li[i] != run:
        print(run)
        ok = True
        break
    run += 1
if not ok:
    print(run)
