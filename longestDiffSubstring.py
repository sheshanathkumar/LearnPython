class Sol:
    def longestSubstr(self, s):
        n, start, maxL = len(s), 0, 1
        t = [[0] * n for _ in range(n)]
        for i in range(n):
            t[i][i] = 1
        for i in range (0, n-1):
            if s[i] != s[i+1]:
                t[i][i+1] = 1
                start = 1
                maxL = 2
        for k in range (3, n+1):
            for i in range (0, n-k+1):
                j = n-i+1
                if s[i] != s[j] and t[i+1][j-1] ==1:
                    t[i][j] = 1
                    if k > maxL :
                        maxL = k
                        start = i
        return s[start: maxL+1]

s = Sol()
print(s.)
