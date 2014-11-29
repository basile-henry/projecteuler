cache = [0] * 1000000

def fac(n):
	if n == 0:
		return 1
	return n * fac(n-1)

def getNext(n):
	return sum([fac(int(l)) for l in str(n)])

def getChainSize(n):
	l = [n]
	t = getNext(n)

	while t not in l:
		if l[-1] < 1000000:
			if cache[l[-1]] != 0:
				return len(l) - 1 + cache[l[-1]]

		l.append(t)
		t = getNext(l[-1])

	cache[n] = len(l)
	return len(l)

s = 0

for i in range(1000000):
	if getChainSize(i) == 60:
		s += 1
		print s, i