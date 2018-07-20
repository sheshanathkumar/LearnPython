#Find element in sorted rotated array
def findArrPivot(arr, l, h, x):
	if l > h:
		return -1
	else :
		mid = int((l+h)/2)
		if arr[mid-1] < arr[mid] > arr[mid+1]:
			print(mid)
			if arr[0] <= x <= arr[mid] :
				f = findElement(arr, 0, mid, x)
				if f != -1 :
					print (f)
				else :
					print("OOPS!")
			elif arr[mid+1] >= x >= arr[h]:
				f = findElementR(arr, mid+1, h, x)
				if f != -1:
					print (f)
				else :
					print("OOPS!")
			else:
				print("OOPS!")
		elif arr[mid-1] < arr[mid] < arr[mid+1]:
			findArrPivot(arr, mid+1, h, x)
		else:
			findArrPivot (arr, l, mid - 1, x)
	

def findElement (arr, l, h, x) :
	if l > h:
		return -1
	mid = int ((l+h)/2)
	if arr[mid] == x :
		return mid
	elif arr[mid] > x :
		findElement (arr, l, mid, x)
	else :
		findElement(arr, mid, h, x)

def findElementR(arr, l, h, x):
	if l > h:
		return -1
	mid = int ((l+h)/2)
	if arr[mid] == x :
		return mid
	elif arr[mid] < x :
		findElementR (arr, l, mid-1, x)
	else :
		findElementR (arr, mid+1, h, x)



t = int(input())
while t != 0:
	n,x = map(int, input().split())
	arr = list(map(int, input().strip().split()))
	findArrPivot (arr, 0, n-1, x)


	t -= 1