for _ in range(int(input())):
    n, m = map(int, input().split())
    li = list(map(int, input().split()))
    a = max(li)
    for i in range(len(li)):
        if li[i] == a:
            li.insert(i, m)
            break
    arr1 = []
    arr2 = []
    for i in li:
        if i < 0:
            arr1.append(i)
        else:
            arr2.append(i)
    for i in arr1:
        print(i, end=" ")
    for i in arr2:
        print(i, end=" ")
    print()
