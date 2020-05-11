#Show 2nd max freequency number

from collections import Counter

t = int(input())
while t > 0:
    s = int(input())
    words = list(map (str, input().strip().split()))
    my_dict = dict(Counter(words))
    print(my_dict)
    a = sorted(my_dict.items(), key=lambda x: x[1])
    print(a)
    print(a[len(a)-2][0])
    t = t-1