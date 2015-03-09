import primes

def rotate(n, x):
	return int(str(n)[x:] + str(n)[0:x])

def getRotations(n):
	return [rotate(n,i) for i in range(len(str(n)))]

print sum([1 for i in primes.getPrimesBetween(2,101) if all([primes.isPrime(r) for r in getRotations(i)])])
