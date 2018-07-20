def findSubs (s):
	n = len(s)
	sets = {''}
	for i in range (n):
		for j in range (i, n):
			sets.add(s[i:j+1])

	print(sets)
	print (len(sets)-1)

findSubs("abaa")
