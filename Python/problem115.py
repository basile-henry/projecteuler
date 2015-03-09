cache = [[0 for i in range(10000)] for i in range(10000)]

def howManyIn(min, x, n):
	if n < x:
		return 0

	if cache[x][n] > 0:
		return cache[x][n]

	cache[x][n] = 0

	for i in range(n-x+1):
		cache[x][n] += 1
		for j in range(min, n+1):
			cache[x][n] += howManyIn(min, j, n-i-x-1)

	return cache[x][n]

def F(min, n):
	return 1 + sum([howManyIn(min, i, n) for i in range(min, n+1)])

i = 55


while F(50,i) < 1000000:
	i+=1
	print i, F(50,i)