from datetime import datetime


class Gamer:
    def __init__(self, code, name, st, en):
        self.code = code
        self.name = name
        self.time = (datetime.strptime(en, "%H:%M") - datetime.strptime(st, "%H:%M")).seconds
        self.h = self.time // 3600
        self.m = (self.time // 60) % 60

    def __str__(self):
        return self.code + " " + self.name + " " + f"{self.h} gio {self.m} phut"


li = []
for _ in range(int(input())):
    li.append(Gamer(input(), input(), input(), input()))

li.sort(key=lambda x: (-x.time))
for i in range(len(li)):
    print(li[i])
