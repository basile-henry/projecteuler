from primes import *

h = getCloserPrimeIndex(1000000)

m = 0
p = 0

for a in range(h):
	s = 0
	for b in range(a,h+1):
		s+=getPrimeAt(b)
		if isPrime(s) and b-a > m:
			m = b-a
			p = s
			print p, m

		if s>1000000:
			break
