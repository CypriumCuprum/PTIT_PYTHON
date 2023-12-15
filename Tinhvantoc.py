class Cuarer:
    def __init__(self, name, province, time):
        ok = (province + " " + name).split()
        self.id = ""
        for i in ok:
            self.id += i[0].upper()
        self.name = name
        self.province = province
        # timee = (datetime.strptime(time, '%H:%M') - datetime.strptime('6:00', '%H:%M')).seconds / 3600
        # self.speed = round(120 / (timee))
        self.timee = (int(time[0]) - 6) + int(time[-2:]) / 60
        self.speed = round(120 / (self.timee))

    def __str__(self):
        return "{} {} {} {} Km/h".format(self.id, self.name, self.province, str(self.speed))


li = []
for _ in range(int(input())):
    li.append(Cuarer(input(), input(), input()))

li.sort(key=lambda x: x.timee)
for i in li:
    print(i)
