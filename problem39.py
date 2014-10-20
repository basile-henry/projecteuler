def getTriangles(n):
	t = []
	for i in range(n):
		for j in range(n-i):
			k = n - i - j

			if (k**2 == i**2 + j**2 or i**2 == k**2 + j**2 or j**2 == k**2 + i**2) and (not sorted([i,j,k]) in t) and k!=0 and j!=0 and i!=0:
				t.append(sorted([i,j,k]))
	return t

m = 0
v = 0

for i in range(1001):
	x = len(getTriangles(i))
	if m < x:
		m = x
		v = i

print v