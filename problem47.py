import primes

def getPrimeDivisors(n):
	
	divs = []

	while n != 1:
		i = 0
		p = 2

		while n%p != 0 and p<n:
			i+=1
			p = primes.getPrimeAt(i)

		divs.append(p)
		n/=p

	return divs

def count(v, l):
	return sum([1 for e in l if e == v])

def getPrimeFactors(n):
	out = []
	x = getPrimeDivisors(n)

	for i in list(set(x)):
		c = count(i,x)
		if c == 1:
			out.append(i)
		else:
			out.append(i**c)

	return out


# def diff(a, b):
# 	out = []
# 	for aa in a:
# 		if aa in b:
# 			b.remove(aa)
# 		else:
# 			out.append(aa)
# 	return out

def hasFourDistinct(a,b):
	if len(set(a)-set(b)) < 4:
		return False
	if len(set(b)-set(a)) < 4:
		return False
	return atLeastFourDiff(a) and atLeastFourDiff(b)

def atLeastFourDiff(l):
	return len(set(l)) >= 4

def haveFourDistinct(l):
	for e in l:
		for f in l:
			if e != f and not hasFourDistinct(e,f):
				return False
	return True

t = 1

while not haveFourDistinct(map(getPrimeFactors,[t, t+1, t+2, t+3])):
	t += 1
	print t


print t, map(getPrimeFactors,[t, t+1, t+2, t+3])
