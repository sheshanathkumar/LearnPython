#Hackerrank Finding the percentage
n = (int) (input())
marksheet = [input().strip().split() for _ in range(n)]
name = input()
res= [i for i in marksheet if i[0] == name]
x = (float(res[0][1]) + float(res[0][2]) + float(res[0][3])) / 3
print( "{:.2f}".format(x))