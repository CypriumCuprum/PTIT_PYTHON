from decimal import Decimal, ROUND_HALF_UP
from functools import reduce


class Hs:
    def __init__(self, id, name, mark):
        self.id = id
        self.name = name
        self.mark = mark
        self.settb()
        self.setxl()

    def settb(self):
        self.tb = (self.mark[0] * 2 + self.mark[1] * 2 + reduce(lambda x, y: x + y, self.mark[2:])) / 12
        self.tb = (self.tb).quantize(Decimal('0.1'), rounding=ROUND_HALF_UP)
        #

    def setxl(self):
        if self.tb >= 9:
            self.xl = 'XUAT SAC'
        elif self.tb >= 8:
            self.xl = "GIOI"
        elif self.tb >= 7:
            self.xl = "KHA"
        elif self.tb >= 5:
            self.xl = "TB"
        else:
            self.xl = "YEU"

    def toString(self):
        return self.id + " " + self.name + " " + str(self.tb) + " " + self.xl

    def __lt__(self, other):
        if self.tb == other.tb:
            return self.id < other.id
        return self.tb > other.tb


arr = []
for i in range(1, int(input()) + 1):
    name = input()
    mark = [Decimal(x) for x in input().split()]
    id = "HS{:02d}".format(i)
    hs = Hs(id, name, mark)
    arr.append(hs)
arr = sorted(arr)
for i in arr:
    print(i.toString())
