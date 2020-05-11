#Hackerrank Any or All

s = int (input())
arr = list(map(int, input().strip().split()))
ifPositive = lambda i: all(arr[i] > 0) 
print(ifPositive)