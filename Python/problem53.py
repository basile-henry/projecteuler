def fac(n):
	if n == 0:
		return 1
	return n * fac(n-1)

def ncr(n, r):
	return fac(n)/(fac(r) * fac(n-r))

count = 0

for n in range(1,101):
	for r in range(1, n):
		if ncr(n,r) > 1000000:
			count += 1
			print count