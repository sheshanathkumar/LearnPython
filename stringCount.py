import re
b = "EEEFFFFRREEES"
s = re.sub(r'((.)\2+)', "", b)
print(s)