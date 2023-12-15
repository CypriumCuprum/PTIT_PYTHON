import math


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance(self, p):
        return math.sqrt((self.x - p.x) ** 2 + (self.y - p.y) ** 2)


class Triangle:
    def __init__(self, p1, p2, p3):
        self.v1 = p1.distance(p2)
        self.v2 = p2.distance(p3)
        self.v3 = p3.distance(p1)

    def area(self):
        if self.v1 + self.v2 + self.v3 <= 2 * max([self.v1, self.v2, self.v3]):
            return "INVALID"
        s = self.v1 + self.v2 + self.v3
        return "{ok:.2f}".format(ok=(((s * (s - 2 * self.v1) * (s - 2 * self.v2) * (s - 2 * self.v3)) ** (1 / 2)) / 4))


ll = []
t = int(input())
li = []
for i in range(t): li.extend([float(x) for x in input().split()])
i = 0
for _ in range(t):
    pp1 = Point(li[i], li[i + 1])
    pp2 = Point(li[i + 2], li[i + 3])
    pp3 = Point(li[i + 4], li[i + 5])
    i += 6
    s = Triangle(pp1, pp2, pp3)
    print(s.area())
