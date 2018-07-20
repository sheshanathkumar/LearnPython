def countData(b):
    res = [0] * 27
    underS = False
    for i in range (len(b)):
    	if b[i] == '_':
    		res[26] += 1
    		underS = True

    if underS == True:
    	for i in range (0, len(b)):
    		if b[i] != "_":
    			s = ord(b[i])
    			res[s - 65] += 1

    	happy = True

    	for i in range (0, 26):
    		if res[i] == 1:
    			happy = False
    			break

    else :
    	happy = true
    	for i in range (0, len(b)-1):
    		if i== 0 and b[i] != b[i+1]:
    			happy = False
    			break

    		if b[i-1] != b[i] != b[i+1]:
    			happy = False
    			break

    if happy == True:
    	print("YES")
    else :
    	print("NO")



b = "_"
countData(b)
c = "MKNNNNMMMK"
countData(c)
