col = ['A', 'B', 'C']


def make(st, end, num):
    mid = 3 - st - end
    if num == 1:
        print(col[st] + " -> " + col[end])
    else:
        make(st, mid, num - 1)
        print(col[st] + " -> " + col[end])
        make(mid, end, num - 1)


make(0, 2, int(input()))
