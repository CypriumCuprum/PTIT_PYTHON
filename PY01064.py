def search(pos, n):
    mid = 2 ** (n - 1)
    if pos == mid:
        return chr(65 + n - 1)
    else:
        if pos > mid:
            return search(pos - mid, n - 1)
        else:
            return search(pos, n - 1)


for _ in range(int(input())):
    n, k = map(int, input().split())
    print(search(k, n))
