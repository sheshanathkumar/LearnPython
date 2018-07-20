#Search the element in the soreted rotated array

def binarySearch(arr, l, r, x):
	while l <= r:
		mid = int((l + r) / 2)
		if arr[mid] == x:
			return True;
		elif arr[mid] < x:
			l = mid+1
		else :
			r = mid-1
	return False

def searchElement (arr, n, x):
	for i in range(0, n):
		if(arr[i] > arr[i+1]):
			break
	if arr[i] == x:
		return True
	elif arr[i+1] == x:
		return True
	elif arr[0] <= x and arr[i] > x :
		return binarySearch(arr, 0, i, x)
	elif arr[i+1] < x and arr[n-1] >= x:
		return binarySearch(arr,i+1, n-1, x)
	else :
		return False

arr = [6,7,8,9,1,2,3,4,5]
x = 2
n = len(arr)
if searchElement(arr, n, x) == True :
	print ("Search Complete")
else :
	print ("Element not Found")