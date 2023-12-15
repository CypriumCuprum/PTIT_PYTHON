n, m = map(int, input().split())
matrix = []
MAX,MIN = 0, 10000000000
for i in range(n):
    arr = list(map(int,input().split()))
    MAX = max(MAX, max(arr))
    MIN = min(MIN, min(arr))
    matrix.append(arr)
ans = []
check = True
for i in range(n):
    for j in range(m):
        if matrix[i][j] == MAX-MIN:
            check = False
            ans.append(f'Vi tri [{i}][{j}]')
if check:
    print("NOT FOUND")
else:
    print(MAX-MIN)
    print('\n'.join(ans))