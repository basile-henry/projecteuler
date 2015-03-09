import primes2 as primes

def isPan(n):
	return set(map(int, str(n))) == set(range(1, len(str(n))+1))

for p in primes.primes:
	if isPan(p):
		print p