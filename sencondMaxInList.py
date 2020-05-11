#show second larger element in list
n = (int)(input())
s = set(map(int, input().strip().split()))
m = max(s)
s.remove(m)
print(max(s))

