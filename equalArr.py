t = int(input())
while t > 0:
    s = int(input())
    ar1 = list(map(int, input().strip().split()))
    ar2 = list(map(int, input().strip().split()))
    ar1, ar2=sorted(ar1), sorted(ar2)
    if ar1 == ar2:
        print(1)
    else :
        print(0)
    t = t - 1