from operator import itemgetter
list_student = []

for _ in range(int(input())):
    name = input()
    cor, submit = input().split()
    cor = -int(cor)
    submit = int(submit)
    a_student = {}
    a_student['name'] = name
    a_student['correct'] = cor
    a_student['submit'] = submit
    list_student.append(a_student)

rs = sorted(list_student, key=itemgetter('correct', 'submit', 'name'))

for i in rs:
    print(i['name'], -i['correct'], i['submit'])