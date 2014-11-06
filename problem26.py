def getPeriod(d):
	n = 1
	remainders = []

	while not (n - n/d) in remainders:
		remainders.append((n - n/d))
		n = (n - n/d) * 10

	return len(remainders) - remainders.index(n - n/d)

print getPeriod(7)