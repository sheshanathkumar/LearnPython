#Roatae array by given numbe

arr = [1,2,3,4,5,6,7]
s = 2
b = arr[s-1::-1]
c = arr[:s-1:-1] 
arr = c+b;
print(b)
print(c)
print(arr)
print(arr[::-1], end = ' ')