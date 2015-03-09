import primes2 as primes

def isPairPrime(a, b):
	return primes.isPrime(int(str(a) + str(b))) and primes.isPrime(int(str(b) + str(a)))

def test(l, n):
	return all([isPairPrime(a, n) for a in l])

def next(l, limit):
	i = primes.getIndexOf(l[-1]) + 1
	p = primes.getPrimeAt(i)

	while not test(l, p):
		i+=1
		p = primes.getPrimeAt(i)

		if p > limit:
			return 0

	return primes.getPrimeAt(i)

def buildList(start, limit):
	ret = [start]
	while ret[-1] > 0:
		ret.append(next(ret, limit))

	return ret[:-1]

i = 0
p = []

print primes.primes[-1]
while len(p) < 5:
	p = buildList(primes.getPrimeAt(i), 10000)
	print p, sum(p)
	i+=1