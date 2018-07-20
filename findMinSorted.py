#Find minimum element in sorted rotated array

def findMin(a, l, h):
	if l > h:
		return a[0]
	elif l == h:
		return a[l]
	else :
		mid = int((l + h) / 2)
		if mid > l and a[mid] < a[mid-1]:
			return a[mid]
		elif mid < h and a[mid+1] < a[mid]:
			return a[mid+1]
		elif a[mid] < a[h]:
			return findMin(a, l, mid-1)
		else :
			return findMin(a, mid+1, h)


t = int(input().strip())
while t > 0:
    t -= 1
    n = int(input().strip())
    arr = list(map(int,input().strip().split()))
        
    print(findMin(arr, 0, n-1))