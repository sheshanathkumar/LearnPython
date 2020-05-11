#show all combination of a letter with n k
# from itertools import combinations
# a, n = map(str, input().strip().split())
# for i in range (1, int(n)+1):
#     for j in sorted(combinations(a, i)):
#         print(''.join(j))

# from itertools import combinations_with_replacement
# a, n = map(str, input().strip().split())
# for j in combinations_with_replacement(sorted(a), int(n)):
#     print(''.join(j))


# from itertools import groupby
# a = "1222311";
# for (i, j) in groupby(a):
#     print(*[(len(list(j)), int(i))],end=' ')

# from itertools import combinations, combinations_with_replacement
# a = "aacd";
# l = list(combinations(a,2))
# m = [ i for i in l if "a" in i ]
# print (  round( (len(m)/len(l) ),3))



from itertools import combinations

num = int(input())
arr = map(str,input().strip().split())
ind = int(input())
ss = ''.join(arr)
l = list(combinations(ss, ind))
m = [i for i in l if "a" in i]
print( round( (len(m)/len(l)),5 ) )