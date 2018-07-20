def commonChild(s1, s2):
    l = [[0]* 5001 for i in range (5001)]
    for i in range (1, len(s1)+1) :
        for j in range (1, len(s1)+1):
            if s1[i-1] == s2[j-1]:
                l[i][j] = l[i-1][j-1] + 1
            else :
                l[i][j] = max (l[i-1][j], l[i][j-1])
    return l[len(s1)][len(s2)]

s1 = input()
s2 = input()
result = commonChild(s1, s2)
print(result)
