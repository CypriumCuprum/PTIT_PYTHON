from datetime import datetime

fee = {'1': 25, '2': 34, '3': 50, '4': 80}


class Room:
    def __init__(self, id, name, room, start, end, extra):
        self.name = name
        self.room = room
        self.id = "KH{}".format(str(id).zfill(2))
        self.days = (datetime.strptime(end, "%d/%m/%Y") -
                     datetime.strptime(start, "%d/%m/%Y")).days + 1
        self.total = extra + self.days * fee[self.room[0]]

    def __str__(self):
        return self.id + " " + self.name + " " + self.room + " " + str(self.days) + " " + str(self.total)


ds = []
for i in range(int(input())):
    ds.append(Room(i + 1, input(), input(), input().strip(), input().strip(), int(input())))

ds.sort(key=lambda x: -x.total)
for i in ds:
    print(i)
