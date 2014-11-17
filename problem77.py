from primes import *

def howManySums(n, index):
	p = getPrimeAt(index)

	if n < p:
		return 0
	elif n == p:
		return 1

	return howManySums(n, index + 1) + howManySums(n - p, index)

i = 2

while True:
	i+=1

	print i, howManySums(i, 0)
	if howManySums(i, 0) > 5000:
		break