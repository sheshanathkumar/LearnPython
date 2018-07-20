def plusMinus(arr):
    plus, minus, zero = 0, 0, 0
    for i in range (0, len(arr)):
        if arr[i] > 0:
            plus = plus + 1
        elif arr[i] < 0:
            minus += 1
        else :
            zero += 1
    p = plus / len(arr)
    m = minus / len(arr)
    z = zero / len(arr)
    print("%.6f" % p)
    print("%.6f" % m)
    print("%.6f" % z)


n = int(input())
arr = list(map(int, input().rstrip().split()))
plusMinus(arr)