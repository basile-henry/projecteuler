l = 6

cache = [[0 for x in range(l)] for y in range(10)]

def asc(min, n):
	if n == 0:
		return 1

	if cache[min][n-1] > 0:
		return cache[min][n-1]

	cache[min][n-1] = sum([asc(m, n-1) for m in range(min, 10)])
	return cache[min][n-1]

def getNonBouncies(n):
	s = 0
	for i in range(10):
		s += asc(i, n)
	return 2 * s - 10

print getNonBouncies(l)
print cache