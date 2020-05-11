#change lower case to upper and vice versa
s = 'HackerRank.com presents "Pythonist 2".'
t = ''.join([ x.upper() if x.islower() else x.lower() for x in s])
print(t)
