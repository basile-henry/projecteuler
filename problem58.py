import primes2

jump = 1
corner = 0

c = [1]
p = 0

while True:
	c.append(c[-1] + 2*jump)

	if primes2.isPrime(c[-1]):
		p+=1

	corner = (corner + 1)%4
	if corner == 0:
		r = float(p)/len(c)
		if r < 0.1001:
			print 2*jump + 1, p, len(c), r
			if r < 0.1:
				break

		jump += 1

