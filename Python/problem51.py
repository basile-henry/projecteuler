import primes

def replace(a, b, n):
	return int(str(n).replace(str(a), str(b)))

done = False

for p in primes.primes:
	
	for i in list(set(str(p))):
		l = []
		for x in range(10):
			t = replace(i, x, p)
			if primes.isPrime(t) and len(str(t)) == len(str(p)):
				l.append(t)

		if len(set(l)) == 7:
			print p, list(set(l))
			done = True
			break

	if done:
		break