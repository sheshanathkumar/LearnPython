def inserSort (a) :
	key = 0
	cnt = 0
	for i in range (1, len(a)) :
		key = a[i]
		j = i-1
		while (j >= 0 and a[j] > key):
			cnt += 1
			a[j + 1] = a[j]
			j = j - 1 
		a[j+1] = key
	print(cnt)

a = [2,1,3,1,2]
inserSort(a)

def getMedian(newL) :
    sort(newL)
    if len(newL) % 2 == 1:
        return newL[len(newL) // 2]
    else :
        mid1 = len(newL) // 2
        mid2 = mid1-1
        medd = ( newL[mid1] + newL[mid2] ) / 2
        return medd


        while ( i < len(l1)) :
		a[k] = l1[i]
		k += 1
		i += 1
	while (j < len(l2)):
		a[k] = l2[j]
		k += 1
		j += 1