import math


class P:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance(self, other):
        return math.sqrt((self.x - other.x) ** 2 + (self.y - other.y) ** 2)


for _ in range(int(input())):
    n = int(input())
    k = int(input())
    li = []
    for i in range(n):
        x, y = map(int, input().split())
        li.append(P(x, y))
    # ok = True
    # for i in range(n):
    #     if ok == False:
    #         break
    #     for j in range(i + 1, n):
    #         if ok == False:
    #             break
    #         for l in range(j + 1, n):
    #             O = P((li[i].x + li[j].x + li[l].x) / 3, (li[i].y + li[j].y + li[l].y) / 3)
    #             d = O.distance(li[i])
    #             cnt = 0
    #             for z in range(n):
    #                 if z == i or z == j or z == l:
    #                     continue
    #                 if d > O.distance(li[z]):
    #                     cnt += 1
    #             if cnt == k:
    #                 ok = False
    #                 print("YES")
    #                 break
    # if ok:
    #     print("NO")
