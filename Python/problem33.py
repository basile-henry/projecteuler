primes = [2]
i = 3

while primes[-1] < 100:
	isPrime = True

	for p in primes:
		if i%p == 0:
			isPrime = False
			break

	if isPrime:
		primes.append(i)
	i+=1

def mult(a):
	if a == []:
		return 1
	return a[0] * mult(a[1:])

def diff(a, b):
	out = []
	for aa in a:
		if aa in b:
			b.remove(aa)
		else:
			out.append(aa)
	return out

def getPrimeDivisors(n):
	
	divs = []

	while n != 1:
		i = 0

		while n%primes[i] != 0 and primes[i]<n:
			i+=1

		divs.append(primes[i])
		n/=primes[i]

	return divs

def getReducedFraction(n,d):
	n = getPrimeDivisors(n)
	d = getPrimeDivisors(d)

	return [mult(diff(n[:],d[:])), mult(diff(d[:],n[:]))]

def dumbSimplify(a,b):
	if '0' in str(a) or '0' in str(b):
		return [a,b]

	out_a = "".join(diff(list(str(a)),list(str(b))))
	out_b = "".join(diff(list(str(b)),list(str(a))))

	if out_a == "":
		out_a = "1"
	if out_b == "":
		out_b = "1"
	return [int(out_a), int(out_b)]

l = []

for a in range(10,100):
	for b in range(a+1,100):
		x = dumbSimplify(a,b)
		if getReducedFraction(a,b) == getReducedFraction(x[0],x[1]) and x != [a,b]:
			l.append([a,b])

print getReducedFraction(mult([x[0] for x in l]), mult([x[1] for x in l]))[1]