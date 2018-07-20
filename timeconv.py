def timeconv(s) :
	n = len(s)
	hh, mm, ss = 0, 0, 0
	for i in range(0,2):
		hh = hh * 10 + int(s[i])
	for i in range (3, 5):
		mm = mm * 10 + int(s[i])
	for i in range (6, 8):
		ss = ss * 10 + int(s[i])
	if (s[n-2] == 'P' and hh != 12):
		hh = hh + 12
	if (s[n-2] == 'A' and hh == 12):
		hh = 0
	st = ''
	if hh < 10:
		st = '0' + str(hh)
	else :
		st = str(hh)
	if mm < 10:
		st = st + ':' + '0' + str(mm)
	else :
		st = st + ':' +str(mm)
	if ss < 10:
		st = st + ':' + '0' + str(ss)
	else :
		st = st + ':' + str(ss)

	return st

s = input()
res = timeconv (s)
print(res)