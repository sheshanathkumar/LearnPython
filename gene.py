def gene(s):
    g = {'A': 0, 'T': 0, 'C': 0, 'G': 0}
    for i in s:
        g[i] += 1

    l, r, minm = 0,0,9999999
    while (r < len(s)):
        c = s[r]
        g[c] -= 1
        r += 1
        while (isSteady(g, len(s))):
            minm = min (minm, r-l)
            cc = s[l]
            g[cc] += 1
            l += 1
    return minm

def isSteady(g, n):
    for i in g:
        if g[i] > n//4 :
            return False
    return True

    

t = int(input())
s = input()
res = gene(s)
print(res)
