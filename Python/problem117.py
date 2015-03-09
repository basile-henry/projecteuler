cache = [[0 for i in range(51)] for i in range(5)]

def howManyIn(x, n):
	if n < x:
		return 0

	if cache[x][n] > 0:
		return cache[x][n]

	cache[x][n] = 0

	for i in range(n-x+1):
		cache[x][n] += 1 + howManyIn(2, n-i-x) + howManyIn(3, n-i-x) + howManyIn(4, n-i-x)

	return cache[x][n]

x = 50
print 1 + howManyIn(2, x) + howManyIn(3, x) + howManyIn(4, x)