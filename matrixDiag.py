def solve (a):
	lDiag, rDiag = 0, 0
	for i in range (0, len(a)) :
		for j in range (0, len(a)) :
			if (i == j):
				lDiag = lDiag + a[i][j]
			if (i + j == n-1):
				rDiag = rDiag + a[i][j]
	res= abs (rDiag - lDiag)
	return res

a = []
n = int(input())
for i in range(0, n):
    a.append(list(map(int, input().strip().split())))
res = solve (a)
print (res)