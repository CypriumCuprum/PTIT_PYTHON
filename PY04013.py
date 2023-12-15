from datetime import datetime


class Location:
    def __init__(self, name, st, en, quantity, code="0"):
        self.name = name
        self.code = code
        self.time = (datetime.strptime(en, "%H:%M") - datetime.strptime(st, "%H:%M")).seconds / 3600
        self.quantity = quantity

    def __str__(self):
        return self.code + " " + self.name + " " + "{p:.2f}".format(p=self.quantity / self.time)


dic = {}
li = []
run = 1
for _ in range(int(input())):
    name = input()
    st = input()
    en = input()
    quantity = int(input())
    a = Location(name, st, en, quantity)
    if name in dic:
        k = dic[name]
        li[k].time += a.time
        li[k].quantity += a.quantity
    else:
        a.code = "T{}".format(str(run).zfill(2))
        dic[name] = run - 1
        run += 1
        li.append(a)

for i in range(len(li)):
    print(li[i])
