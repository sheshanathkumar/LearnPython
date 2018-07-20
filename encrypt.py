import math



def encrypt (s) :
	x = len(s)
	r = math.ceil(math.sqrt(x))
	c = math.floor(math.sqrt(x))
	str = ""
	for j in range (r):
		i = j
		while ( i < x):
			str = str + s[i]
			i += r
		str = str + " "
	return str




s = "haveaniceday"
res = encrypt (s)
print (res, end="")
