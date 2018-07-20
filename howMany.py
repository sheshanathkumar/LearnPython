def findSubs (s, l, h):
	sets = {""}
	ts = ""
	for i in range (l, h+1):
		ts = ts + s[i]
	n = len (ts)
	print(ts)
	size = len(ts) ** 2
	
	for i in range (0, size) :
		p = ""
		for j in range (0, n) :
			if i & (1 << j) > 0:
				p = p + ts[j]
		
		if ts.count(p) != 0:
			sets.add(p) 



	print(sets)



findSubs ("aabaa", 1,1)
