class Student:
    def __init__(self, name, theory, practice, code):
        self.name = name
        if theory > 10:
            theory = float(theory / 10)
        if practice > 10:
            practice = float(practice / 10)
        self.mean = (practice + theory) / 2
        self.code = code
        if self.mean < 5:
            self.rank = "TRUOT"
        elif self.mean < 8:
            self.rank = "CAN NHAC"
        elif self.mean < 9.5:
            self.rank = "DAT"
        else:
            self.rank = "XUAT SAC"

    def __str__(self):
        return self.code + " " + self.name + " " + "{para:.2f}".format(para=self.mean) + " " + self.rank


li = []
run = 1
for _ in range(int(input())):
    li.append(Student(input(), float(input()), float(input()), "TS0{}".format(str(run))))
    run += 1

li.sort(key=lambda x: (-x.mean))
for i in range(len(li)):
    print(li[i])
