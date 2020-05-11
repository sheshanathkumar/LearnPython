import math

t = int(input())
while t > 0:
    row, col = map(int, input().strip().split())
    val1 = math.factorial(row + col);
    val2 = math.factorial(row) * math.factorial(col) 
    val = val1 // val2
    print(val)
    t = t-1