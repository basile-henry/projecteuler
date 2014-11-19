def isPan(n):
	return set(str(n)) == set("123456789") and len(str(n)) == 9


m = 0

for i in range(100000):
	n = ""
	j = 1
	while len(n)<9:
		n = n + str(i*j)
		j+=1

	if isPan(n):
		print n
		if int(n)>m:
			m = int(n)

print "max:", m