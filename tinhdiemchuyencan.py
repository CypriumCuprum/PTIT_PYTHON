class SV:
    def __init__(self, idcode, name, classroom):
        self.name = name
        self.idcode = idcode
        self.classroom = classroom

    def __str__(self):
        return self.idcode + " " + self.name + " " + self.classroom


def setpoint(point):
    p = 10
    for i in range(len(point)):
        if point[i] == 'm':
            p -= 1
        elif point[i] == 'v':
            p -= 2
    if p <= 0:
        return "0 KDDK"
    return str(p)


dic = {}
ds = []
t = int(input())
for i in range(t):
    ds.append(SV(input(), input(), input()))
for i in range(t):
    msv, point = map(str, input().split())
    dic[msv] = setpoint(point)
for i in ds:
    print(i, end=" ")
    print(dic[i.idcode])
