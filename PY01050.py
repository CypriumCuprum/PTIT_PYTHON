n = int(input())

rs = ['A' for _ in range(n+1)]
letter = ['A','B','C']
dic = {}

def check(k):
    dic['A'] = 0
    dic['B'] = 0
    dic['C'] = 0
    for i in rs[:k]:
        dic[i] += 1
    if dic['A'] == 0 or dic['B'] == 0 or dic['C'] == 0:
        return False
    if dic['A'] > dic['B'] or dic['B'] > dic['C']:
        return False
    return True


def inn(k):
    innn = ''
    for i in rs[:k]:
        innn += i
    print(innn)


def gen(i, k):
    if i >= k:
        if check(k):
            inn(k)
        return
    for t in letter:
        rs[i] = t
        gen(i+1, k)

for i in range(3,n+1):
    gen(0,i)