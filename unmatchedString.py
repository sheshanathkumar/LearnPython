t = int(input())
while t > 0 :
    s1 = input()
    s2= input()
    set1 = set(filter (lambda x : (x not in s2), s1))
    set2 = set(filter (lambda x : (x not in s1), s2))
    word = list(list(set1) + list(set2))
    ans = ''.join((map(str, sorted(word))))
    print(ans)
    t = t-1