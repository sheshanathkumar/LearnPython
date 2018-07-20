global result
global cnt
global k
result= []
k = 1
cnt = 0

def find (k, t, s):
    flag = False
    for i in range (0, len(s)):
        if s[i] != 0 and s[i] == t[i]:
            flag = True
        elif s[i] != 0 and s[i] != t[i]:
            flag = False
            break
    if flag == True:
        return k

def perm(li, s):
    if li == [] or li == None:
        return
    if len(li) == 1:
        result.append(li[0])
        t = result
        f = find(k, t, s)
        cnt += f
        k += 1
        print (t)
        result.pop()

    for i in range(0,len(li)):
        result.append(li[i])
        perm(li[:i] + li[i+1:], s)
        result.pop()

    print(k)
    
s = [0, 2, 3, 0]
li = [1,2,3,4]
perm(li, s)
