t = int(input())
while t > 0:
    size = int(input())
    arr = list(map(int, input().strip().split()))
    print(*(arr[len(arr)::-1]))
    t = t-1