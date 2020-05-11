def getVal(num):
    if num != 0 :
        return max(num, (getVal(num//2) + getVal(num//3) + getVal(num//4)))
    else:
        return 0

t = int(input())
while t > 0:
    num = int(input())
    ans = getVal(num)
    print(ans)
    t = t-1
