primes = [2]
i = 3

while primes[-1] < 100000:
	isPrime = True

	for p in primes:
		if i%p == 0:
			isPrime = False
			break

	if isPrime:
		primes.append(i)
	i+=1


m = 0
best_a = 0
best_b = 0

for a in range(-999,1000):
	for b in range(-999,1000):
		n=0
		while (n**2 + a*n + b) in primes:
			n+=1

		if n>m:
			m = n
			best_a = a
			best_b = b
	print a, m

print m, best_a, best_b, best_a*best_b