#Find element in sorted rotated array
def findArrPivot(arr, l, h):
	while l > h:
		mid = int((l+h)/2)
		if arr[mid-1] < arr[mid] > arr[mid+1]:
			return mid
		elif arr[mid - 1] < arr[mid] < arr[mid+1] :
			l = mid + 1
		elif arr[mid-1] > arr[mid] > arr[mid+1]:
			h = mid - 1

def findElement (arr, l, h, x) :
	while l < h :
		mid = int((l+h)/2)
		if arr[mid] == x:
			print(mid)
			return
		elif arr[mid] > x:
			h = mid - 1
		else:
			l = mid + 1

def findElementR(arr, l, h, x):
	while l < h :
		mid = int((l+h)/2)
		if arr[mid] == x:
			print(mid)
			return 
		elif arr[mid] < x:
			h = mid - 1
		else:
			l = mid + 1



t = int(input())
while t != 0:
	n, x = input().split()
	arr = list(map(int, input().strip().split()))
	#ele = findArrPivot(arr, 0, n-1)
	#if arr[0] <= x <= arr[ele] :
	#	findElement (arr, 0, ele, x)
	#elif arr[ele + 1] >= x >= arr[n-1]:
	#	findElementR (arr, ele+1, n-1, x)
	#else :
	#	print("OOPS!")

	findElement ()


	t -= 1