t = int(input())
while t > 0 :
    size, rot = map(int, input().strip().split())
    arr = list(map(int, input().strip().split()))
    print(*(arr[rot%size:]+ arr[:rot%size]))
    t = t-1
