from collections import Counter

t = int(input())
while t != 0:
    str1, str2 = map(str, input().strip().split())
    str1dict = dict(Counter(str1))
    str2dict = dict(Counter(str2))

    str1Touple = sorted(str1dict.items(), key=lambda x : x[0])
    str2Touple = sorted(str2dict.items(), key=lambda x : x[0])
    
    if str1Touple == str2Touple:
        print('YES')
    else :
        print('NO')
    t = t-1