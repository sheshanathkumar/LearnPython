from collections import Counter

t = int(input())
while t > 0:
    i = int(input())
    words = list(map(str, input().strip().split()))
    my_dict = dict(Counter(words))
    print(my_dict)
    cnt = 0
    for word in my_dict:
        if my_dict[word]==2:
            cnt = cnt+1
    print(cnt)
    t = t-1