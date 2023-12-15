class Customer:
    def __init__(self, name, old, new, code):
        self.code = code
        self.name = name
        self.quantity = new - old
        if self.quantity <= 50:
            self.total = self.quantity * 102
        elif self.quantity <= 100:
            self.total = 50 * 100 + (self.quantity - 50) * 150
            self.total *= (103 / 100)
        else:
            self.total = 50 * 100 + 50 * 150 + (self.quantity - 100) * 200
            self.total *= (105 / 100)

    def __str__(self):
        return self.code + " " + self.name + " " + str(round(self.total))


li = []
run = 1
for _ in range(int(input())):
    li.append(Customer(input(), int(input()), int(input()), "KH{}".format(str(run).zfill(2))))
    run += 1

li.sort(key=lambda x: (-x.total))
for i in range(len(li)):
    print(li[i])
