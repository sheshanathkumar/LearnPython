def kerp(p, q) :

	no = "INVALID RANGE"
	res = []
	for i in range (p, q+1):
		val = i ** 2
		valS = str (val)
		l = len(valS)
		mid = ( l // 2 ) - 1
		part1 = valS[0:mid+1]
		part2 = valS[mid+1:l]
		p1 = int (part1)
		p2 = int (part2)
		if i == p1 + p2:
			res.append(i)

	if (len(res) != 0):
		print(res)
	else :
		print (no)

p = int(input())
q = int(input())
kerp(p, q)

