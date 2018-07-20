import re
f1 = open('input.txt', 'r')
f2 = open('output.txt', 'w')
reg = "^[6-9]\d{9}"
for line in f1:
    list = re.findall(reg, line)
    for num in list:
        f2.write(str(num+ "\n"))

f1.close()
f2.close()
 
