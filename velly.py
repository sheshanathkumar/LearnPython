import os


def velly(s):
    noZero, lvl = 0, 0
    for i in s:
        if s[i] == 'U':
            lvl += 1
        else:
            lvl += -1
        if (lvl == 0):
            noZero += 1

    return noZero


fptr = open(os.environ['res.txt'], 'w')
n = int(input())
s = input()
res = velly(s)
fptr.write(str(res) + '\n')
fptr.close()
