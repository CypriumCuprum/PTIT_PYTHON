

def make(pos, n, runsum, li, visited, ok, sum):
    cnt = 0
    for i in range(pos, n):
        if visited[i] == 0:
            visited[i] = 1
            if int(li[i]) == runsum:
                if ok == 0:
                    cnt += make(0, n, sum, li, visited, ok+1, sum)
                if ok == 1:
                    cnt += 1
            elif int(li[i]) < runsum:
                cnt += make(i+1, n, runsum-int(li[i]), li, visited, ok, sum)
            visited[i] = 0
    return cnt


for _ in range(int(input())):
    n = int(input())
    li = input().split()
    visited = [0 for _ in range(20)]
    sum = 0
    for i in li:
        sum += int(i)
    if sum % 3 == 0:
        k = round(sum/3)
        print(make(0, n, k, li, visited, 0, k))
    else:
        print(0)
