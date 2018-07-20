def merge (a, l, mid, h):
	l1 = []
	for i in range (l, mid+1):
		l1.append(a[i])
	l2 = []
	for i in range (mid+1, h+1) :
		l2.append(a[i])
	     
	i, j, k = 0, 0 ,l
	while (i < len(l1) and j < len(l2)):
		if (l1[i] <= l2[j]) :
			a[k] = l1[i]
			i += 1
		else :
			a[k] = l2[j]
			j += 1
		k += 1
	while ( i < len(l1)) :
		a[k] = l1[i]
		k += 1
		i += 1
	while (j < len(l2)):
		a[k] = l2[j]
		k += 1
		j += 1

	print(a)



def mergeSort (a, l, h) :
	if l < h :
		mid = (l + h ) // 2
		mergeSort (a, l, mid)
		mergeSort (a, mid+1, h)
		merge (a, l, mid, h)

a = [2, 3, 1, 4, 5, 6, 7, 9, 8, 10]
mergeSort (a, 0, len(a)-1)