def getPeriod(d):
	n = 10
	remainders = []

	while not n%d in remainders:
		if n%d == 0:
			return 0
		remainders.append(n%d)
		n = n%d * 10

	return len(remainders) - remainders.index(n%d)

m = 0

for i in range(1,1000):
	if getPeriod(i) > m:
		m = getPeriod(i)
		print i, m