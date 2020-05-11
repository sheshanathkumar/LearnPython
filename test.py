import math

found=False
for i in range(123, 667):
    num = i
    val = i
    while num != 0:
        a = num // 100
        num = num % 100
        b = num // 10
        num = num % 10
        c = num // 1
        num = num % 1
        if val == math.factorial(a) + math.factorial(b) + math.factorial(c):
            print(val)
            found=True
            break
    if found==True:
        break


            

        