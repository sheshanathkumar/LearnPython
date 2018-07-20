#Rotate Array by given number

def rotate(arr, val):
	reverse(arr, 0, val-1)
	reverse(arr, val, len(arr)-1)
	reverse(arr, 0, len(arr)-1)

def reverse(arr, start, end):
	while start <= end:
		arr[start], arr[end] = arr[end], arr[start]
		start = start + 1
		end = end-1




t = int(input())
while t > 0:
	n = int(input())
	arr = []
	arr = input().split()
	val = int(input())
	rotate (arr,val)
	print(arr)
	t = t-1
