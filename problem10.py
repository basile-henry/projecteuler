import primes
s = 0

for x in primes.primes:
	if x < 2000000:
		s+=x
print s