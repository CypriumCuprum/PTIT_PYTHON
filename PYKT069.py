from datetime import datetime

arr = []
f = open("CATHI.in", 'r')


class Cathi:
    def __init__(self, run, s, s1, s2):
        self.code = 'C' + str(run).zfill(3)
        self.date = s
        self.hm = s1
        self.time = datetime.strptime(s + " " + s1, "%d/%m/%Y %H:%M")
        # self.time = datetime.strptime(s + " " + s1, "%d/%m/%Y %H:%M")
        self.id = s2

    def __str__(self):
        return self.code + " " + self.date + " " + self.hm + " " + self.id


for i in range(int(f.readline())):
    arr.append(Cathi(i + 1, f.readline().strip(), f.readline().strip(), f.readline().strip()))

arr.sort(key=lambda x: (x.time, x.code))
for i in arr:
    print(i)
