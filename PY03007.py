def nomalize(s):
    rs_list = s.split()
    rs = ""
    for i in rs_list:
        if i != "":
            rs += (i.lower()+" ")
    print(rs[:1].upper() + rs[1:])


full_text = ""
while True:
    try:
        full_text += input()
    except EOFError:
        break

start = 0
li = ['?', '.', '!']
for i in range(len(full_text)):
    if full_text[i] in li:
        nomalize(full_text[start:i])
        start = i+1


