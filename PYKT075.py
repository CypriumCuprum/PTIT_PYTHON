class Cuocgoi:
    def __init__(self, date, name, phone):
        self.date = date
        self.name = name.split()
        self.phone = phone

    def __str__(self) -> str:
        return "{}: {} {}".format(" ".join(self.name), self.phone, self.date)


lis = []
date = ""
try:
    f = open("SOTAY.txt", 'r')
except:
    f = 0

lines = [x.strip() for x in f if x.strip() != ""]
run = 0
while run < len(lines):
    x = lines[run]
    if x.count('/') > 0:
        date = x.split()[1]
    else:
        lis.append(Cuocgoi(date, x, lines[run + 1]))
        run += 1
    run += 1
lis.sort(key=lambda x: (x.name[2], x.name[1]))
for i in lis:
    print(i)
