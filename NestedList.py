#Hackerrank Nested List
a = (int)(input())
marksheet = [ [input(), float(input())] for _ in range(a)]
marksheet = sorted(marksheet, key=lambda x : x[1])
min_mark = marksheet[0][1]
new_marksheet = [ x for x in marksheet if x[1] != min_mark  ]
min_mark = new_marksheet[0][1]
new_mark = [ x[0] for x in new_marksheet if x[1] == min_mark  ]
print(*(sorted(new_mark)), sep="\n")