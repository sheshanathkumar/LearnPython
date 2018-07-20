def miniMaxSum(arr):
    val = []
    for i in range (0, len(arr)):
        sum = 0
        for j in range (0, len(arr)):
            if j != i :
                sum = sum + arr[j]
        val.append(sum)
    print (min(val), max(val))

arr = list(map(int, input().rstrip().split()))
miniMaxSum(arr)