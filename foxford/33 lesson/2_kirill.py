n = int(input())
q = [-10**4]*11
q1 = [-10**4]*11
k = 0
tup = {0:10,1:4,2:2,3:8,4:1,5:10,6:9,7:2,8:3,9:6}
tup2 = {0:10,1:10,2:7,3:10,4:6,5:10,6:4,7:10,8:10,9:10}
for i in range(n):
	x = int(input())
	if x >= 0:
		r = x % 10
		for u in (q[tup[r]]+x,q[tup2[r]]+x):
			if u > k:
				k = u
		if q[r] < x:
			q[r] = x
	else:
		x=-x
		r = x % 10
		for u in (q1[tup[r]]+x,q1[tup2[r]]+x):
			if k <= 0 and u > k:
				k = u
		if q1[r] < x:
			q1[r] = x
		k = 'отрицательное число'
print(k)
