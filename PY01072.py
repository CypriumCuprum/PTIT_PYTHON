inn = input().split()

n = int(inn[0])
k = int(inn[1])

li = input().split()

# get only one
dic = {}
for i in li:
    if int(i) in dic:
        dic[int(i)] += 1
    else:
        dic[int(i)] = 0
arr = []
for key in dic.keys():
    arr.append(int(key))

arr = sorted(arr)
arr.insert(0, 0)
n = len(arr)

if k > n-1:
    k = n-1

visited = [0 for _ in range(n)]
choose = [0 for _ in range(k)]
choose[0] = 0

def printt():
    for i in choose:
        print(arr[i], end=" ")
    print()


def make_combination(pos,k,n):
    for i in range(choose[pos-1]+1,n):
        if visited[i] == 0:
            visited[i] = 1
            choose[pos] = i
            if pos == k-1:
                printt()
            else:
                make_combination(pos+1,k,n)
            visited[i] = 0

make_combination(0,k,n)




