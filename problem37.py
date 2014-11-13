import primes

def getTruncated(n):
	out = []
	for i in range(len(str(n))):
		out.append(int(str(n)[:len(str(n))-i]))
		out.append(int(str(n)[i:]))

	return out

s = 0#8897
i = primes.getIndexOf(7)+1
l = []

while len(l) < 11:
	j = primes.getPrimeAt(i)
	if all([primes.isPrime(x) for x in getTruncated(j)]):
		s+=j
		l.append(j)
		print j, s

	i+=1

#3797 8897