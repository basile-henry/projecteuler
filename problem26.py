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

def getPrimeDivisors(n):
	
	divs = []

	while n != 1:
		i = 0

		while n%primes[i] != 0 and primes[i]<n:
			i+=1

		divs.append(primes[i])
		n/=primes[i]

	return divs

print [x for x in getPrimeDivisors(10) if x != 2 and x != 5]