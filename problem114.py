cache = [[0 for i in range(51)] for i in range(51)]

def howManyIn(x, n):
	if n < x:
		return 0

	if cache[x][n] > 0:
		return cache[x][n]

	cache[x][n] = 0

	for i in range(n-x+1):
		cache[x][n] += 1
		for j in range(3, n+1):
			cache[x][n] += howManyIn(j, n-i-x-1)

	return cache[x][n]

x = 50
print 1 + sum([howManyIn(i, x) for i in range(3, x+1)])