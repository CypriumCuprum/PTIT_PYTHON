from datetime import datetime

f = open("CATHI.in", 'r')
f1 = open("MONTHI.in", 'r')
f2 = open("LICHTHI.in", 'r')

ca = []
mon = []
lich = []


class Monthi:
    def __init__(self, code, name, mode):
        self.code = code
        self.name = name
        self.mode = mode


for _ in range(int(f1.readline())):
    mon.append(Monthi(f1.readline().strip(), f1.readline().strip(), f1.readline().strip()))


class Cathi:
    def __init__(self, stt, date, timee, code):
        self.stt = 'C' + str(stt).zfill(3)
        self.date = date
        self.timee = timee
        self.dtime = datetime.strptime(date + " " + timee, "%d/%m/%Y %H:%M")
        self.code = code
        self.name = ""
        self.groupid = ""
        self.num = ""
        self.namecode = ""

    def __str__(self):
        return self.date + " " + self.timee + " " + self.code + " " + self.name + " " + self.groupid + " " + self.num


for i in range(int(f.readline())):
    ca.append(Cathi(i + 1, f.readline().strip(), f.readline().strip(), f.readline().strip()))


class Lichthi:
    def __init__(self, stt, idcode, groupid, num):
        self.stt = stt
        self.idcode = idcode
        self.groupid = groupid
        self.num = num


for _ in range(int(f2.readline())):
    inin = f2.readline().split()
    lich.append(Lichthi(inin[0], inin[1], inin[2], inin[3]))

for i in range(len(ca)):
    for j in range(len(lich)):
        if lich[j].stt == ca[i].stt:
            ca[i].groupid = lich[j].groupid
            ca[i].num = lich[j].num
            ca[i].namecode = lich[j].idcode
            break
    for j in range(len(mon)):
        if ca[i].namecode == mon[j].code:
            ca[i].name = mon[j].name
            break

ca.sort(key=lambda x: (x.dtime, x.stt))
for i in ca:
    print(i)
