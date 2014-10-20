temp = open("primes.txt",'r')
primes = [int(a.split(',')[1]) for a in temp.read().split('\n')]
temp.close()

def getPrimeAt(n):
	return primes[n]

def getPrimesAt(a, b):
	return primes[a:b]

def getIndexOf(p):
	try:
		return primes.index(p)
	except ValueError:
		return -1

def getCloserPrimeIndex(n):
	i = -1
	while i == -1:
		i = getIndexOf(n)
		n-=1
	return i
	
def getPrimesBetween(a, b):
	return primes[primes.index(a):primes.index(b)]

def isPrime(n):
	return n in primes