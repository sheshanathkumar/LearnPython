def bin_search(arr, left, high, key):
    #Code here
    found = False
    while left < high:
        mid = (left+high)//2
        if arr[mid]==key:
            print(mid)
            found = True
            break
        elif arr[mid] < key:
            left = mid
        else :
            high = mid
    if found == False:
        print(-1)

arr = [1,2,3,4,5]
bin_search(arr, 0, len(arr), 4)