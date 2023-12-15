chia = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]
limit = []
choose = [[] * 16]


def update(s):
    cnt1 = 0
    ok = 1
    for i in range(len(s)):
        if s[i] == '1':
            cnt1 += 1
            ok *= limit[i]
    choose[cnt1].append(ok)


def make(x, s):
    if x >= len(limit):
        update(s)
    else:
        for i in range(0, 2):
            s = s[:x] + str(i)
            make(x + 1, s)


def bh_lt(end):
    rs = end
    dau = -1
    for i in range(1, len(limit) + 1):
        for j in choose[i]:
            rs += dau * cnt(end, j)
        dau = -dau
    return rs


def cnt(end, div):
    return end // div


while True:
    li = list(map(int, input().split()))
    if li[0] == -1:
        break
    k = int(input())
    limit = []
    choose = [[] for _ in range(17)]
    for i in chia:
        if i <= k:
            limit.append(i)
        else:
            break
    make(0, "")
    print(bh_lt(li[1]) - bh_lt(li[0] - 1))
