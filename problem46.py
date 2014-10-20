import primes

running = True
i = 9
while running:

	if not primes.isPrime(i) and i%2 == 1:
		index = primes.getCloserPrimeIndex(i)

		passed = False

		for j in range(index+1):
			k = 1
			while i > primes.getPrimeAt(j) + 2* k**2:
				k+=1

			if i == primes.getPrimeAt(j) + 2* k**2:
				passed = True
				break

		if not passed:
			print "dat one", i
			running == False
			break
	print i

	i+=1
