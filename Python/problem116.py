cache = [[0 for i in range(51)] for i in range(5)]

def howManyIn(x, n):
	if n < x:
		return 0

	if cache[x][n] > 0:
		return cache[x][n]

	cache[x][n] = 0

	for i in range(0, n-x+1):
		cache[x][n] += 1 + howManyIn(x, n-i-x)

	return cache[x][n]

print howManyIn(2, 50) + howManyIn(3, 50) + howManyIn(4, 50)