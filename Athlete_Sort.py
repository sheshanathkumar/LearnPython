#Hackerrank Athlete Sort

nm = input().split()

n = int(nm[0])

m = int(nm[1])

arr = []

for _ in range(n):
    arr.append(list(map(int, input().rstrip().split())))
arr = sorted(arr, key= lambda x: x[1])
for i in arr :
    print (*(i), end='\n')
