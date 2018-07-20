def findBest (a1, a2, a3, b1, b2, b3) :
	win = [0, 0]
	if a1 > b1 :
		win[0] = win[0] + 1
	if a1 < b1 :
		win[1] = win[1] + 1
	if a2 > b2 :
		win[0] = win[0] + 1
	if a2 < b2 :
		win[1] = win[1] + 1
	if a3 > b3 :
		win[0] = win[0] + 1
	if a3 < b3 :
		win[1] = win[1] + 1

	return win

a1 = int(input())
a2 = int(input())
a3 = int(input())
b1 = int(input())
b2 = int(input())
b3 = int(input())
s = findBest (a1, a2, a3, b1, b2, b3)
print(s)