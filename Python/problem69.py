def getPrimeDivisors(n):
	
	divs = []
	i = 2

	while n > 1:
		if n%i == 0:
			divs.append(i)
			n /= i
		else:
			i += 1

	return divs

def getRelativePrimes(n):
	divs = getPrimeDivisors(n)

	out = []
	for i in range(n):
		if not any([i%d == 0 for d in divs]):
			out.append(i)

	return out

def totient(n):
	return len(getRelativePrimes(n))

m = 0
best_n = 0

for i in range(2,1000000):
	t = totient(i)

	if t > m:
		m = t
		best_n = i
		
print best_n, m
