def stair (n):
	for i in range (1, n+1):
		print ('%' * (n - i) + '#' * i)
	print(end = "")

n = int (input())
stair(n)