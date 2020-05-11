#Count substring
s = "ABCDCDC"
t = "CDC"
cnt = 0
i = 0

while i < len(s):
    if s.find(t, i, len(s)) != -1:
        cnt = cnt+1
        i = s.find(t, i, len(s)) + 1
    else :
        i = i+1
print(cnt)

