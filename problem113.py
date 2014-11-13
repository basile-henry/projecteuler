cache = [[0 for x in range(102)] for y in range(10)] 

def asc(min, n):
	if n == 1:
		return 10 - n

	if cache[min][n] > 0:
		return cache[min][n]

	cache[min][n] = sum([asc(m, n-1) for m in range(min, 10)])
	return cache[min][n]

print 2*asc(0,10) - 10