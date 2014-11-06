from primes import *

def arePerm(a,b):
	a = map(int,str(a))
	b = map(int,str(b))

	a.sort()
	b.sort()

	return a == b

f = getCloserPrimeIndex(1000) + 1
l = getCloserPrimeIndex(9999)

for i in range(f,l):
	c = getPrimeAt(i)
	for r in range(1,(getPrimeAt(l)-c)/2):
		d, f = c + r, c + 2*r

		if arePerm(c,d) and arePerm(d,f) and isPrime(d) and isPrime(f):
			print c,d,f,r

