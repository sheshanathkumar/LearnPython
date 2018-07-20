##Rearrange Negative and positive numbers

def rearrange (a):
	pos = []
	neg = []
	print(*a, sep = ' ')
	for i in range(len(a)):
		if a[i] < 0:
			neg.append(a[i])
		else :
			pos.append(a[i])
	n,p = 0,0
	res = []
	while p < len(pos) and n < len(neg) :
		res.append(pos[p])
		res.append(neg[n])
		p += 1
		n += 1
	while p < len(pos):
		res.append(pos[p])
		p += 1
	while n < len(neg):
		res.append(neg[n])
		n += 1
	print(*res, sep = ' ')

t = int (input())
while t != 0:
	s = int (input())
	a = list(map(int, input().strip().split()))
	rearrange (a)
	t = t-1