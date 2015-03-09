from primes import *
from operator import itemgetter

def getPrimeDivisors(n):
	
	divs = []
	i = 0
	p = getPrimeAt(0)

	while n > 1:
		if n%p == 0:
			divs.append(p)
			n /= p
		else:
			i += 1
			p = getPrimeAt(i)

	return divs

def mult(l):
	if l == []:
		return 0
	if len(l) == 1:
		return l[0]
	return l[0] * mult(l[1:])

def rad(n):
	return mult(list(set(getPrimeDivisors(n))))

rads = []
for i in range(1, 100001):
	rads.append([i, rad(i)])

rads.sort(key=itemgetter(1,0))

print rads[10000-1]
