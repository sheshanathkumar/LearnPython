#Rearrange Negative and positive numbers using Quick Sort

def rearrange (a):
	i = -1
	n = len(a)
	for j in range (0, n-1):
		if a[j] < 0:
			i = i+1
			a[i] , a[j] = a[j], a[i]
	pos = i + 1
	neg = 0
	print(a, end = ' ')
	print("\n")
	while pos > neg and a[neg] < 0 and pos < n :
		a[pos], a[neg] = a[neg], a[pos]
		pos += 1
		neg += 2
	for i in range (0, n):
		print(a[i], end = ' ')

t = int(input())
while t != 0:
	s = int(input())
	a = list(map(int, input().strip().split()))
	rearrange (a)
	t = t-1