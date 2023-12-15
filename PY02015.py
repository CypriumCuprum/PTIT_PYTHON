def count(arr):
    if arr[0] == arr[1] and arr[1] == arr[2] and arr[2] == arr[3]:
         return 0
    ne = []
    for i in range(4):
        ne.append(abs(arr[i]-arr[(i+1)%4]))
    return count(ne)+1


while True:
    arr = list(map(int, input().split()))
    if arr == [0, 0, 0, 0]:
        break
    print(count(arr))