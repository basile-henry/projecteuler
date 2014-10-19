temp = open("primes.txt",'r')
primes = [int(a.split(',')[1]) for a in temp.read().split('\n')]
temp.close()

def getPrimeAt(n):
	return primes[n]

def getPrimesAt(a, b):
	return primes[a:b]

def getIndexOf(p):
	return primes.index(p)
	
def getPrimesBetween(a, b):
	return primes[primes.index(a):primes.index(b)]

def isPrime(n):
	return n in primes