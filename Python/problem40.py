def getDecimal(n):

	s = ""
	i = 1
	while len(s) < n:
		s += str(i)
		i += 1

	return int(s[n-1])

r = 1

for i in [1,10,100,1000,10000,100000,1000000]:
	r *= getDecimal(i)

print r