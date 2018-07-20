def rotateArr(arr, n):
	i = n-2
	val = arr[n-1]
	while i >= 0:
		arr[i+1] = arr[i]
		i = i-1
	arr[0] = val
	return arr

t = int(input())
while t != 0:
	s = int(input())
	arr = input().split()
	#for i in range(0, s):
	#	val = int(input().split())
	#	arr.append(val)

	if (s == 1) :
		print (arr[0])
	else :
		count = 1
		while len(arr) != 1:
			rotateArr(arr, len(arr))
			if len(arr) > count :
				arr.pop(len(arr)-count)
			else :
				arr.pop(0)
			count = count+1

	print(arr[0])
	t = t-1
