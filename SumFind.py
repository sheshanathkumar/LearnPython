#Find sum in a sorted rotated array

def findSum (arr, n, x):
	for i in range (0, n-1):
		if arr[i] > arr[i+1]:
			break

	l = (i + 1 ) % n;
	r = i;

	while ( r != l) :
		if arr[l] + arr[r] == x :
			return True
		elif arr[l] + arr[r] > x:
			r = ( n + r - 1 )%n
		else :
			l = ( l+1 )% n
	return False


arr = [7, 8, 9, 1, 2, 3]
x = 2
n = len(arr)
if findSum(arr, n, x) == True:
	print("Sum Found")
else :
	print("Not Found")