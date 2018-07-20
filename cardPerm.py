import itertools
def solve(s):
    n = len(s)
    l = [i for i in range(1, n+1)]
    r = list(itertools.permutations(l))
    d = {}
    k = 1
    for i in r:
        d[k] = i
        k += 1
    del r, l
    cnt = 0
    for j in d:
        l = list(d[j])
        i = 0
        flag = False
        while (i < n):
            if s[i] == 0:
                i += 1
            elif s[i] == l[i]:
                flag = True
                i += 1
            else :
                flag = False
                break
        if flag == True:
            cnt += j
                
    return cnt


s = int(input())
a = list(map(int, input().rstrip().split()))
res = solve(a)
print(res)
