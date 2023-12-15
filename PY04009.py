class Com:
    def __init__(self, m, n):
        self.a = m
        self.b = n

    def add(self, other):
        newa = self.a + other.a
        newb = self.b + other.b
        return Com(newa, newb)

    def pro(self, p):
        newa = self.a * p.a - self.b * p.b
        newb = self.b * p.a + self.a * p.b
        return Com(newa, newb)

    def toString(self):
        s = str(self.a)
        if self.b > 0:
            s = s + " + " + str(self.b) + "i"
        if self.b < 0:
            s = s + " - " + str(abs(self.b)) + "i"
        return s


for _ in range(int(input())):
    a, b, c, d = map(int, input().split())
    A = Com(a, b)
    B = Com(c, d)
    C = A.add(B).pro(A)
    D = (A.add(B)).pro((A.add(B)))
    print(C.toString() + ", " + D.toString())
