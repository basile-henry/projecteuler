def getPrimeDivisors(n):
	
	divs = []
	i = 2

	while n > 1:
		if n%i == 0:
			divs.append(i)
			n /= i
		else:
			i += 1

	return divs

def reduced(n,d):
	den = getPrimeDivisors(d)
	l = []

	for i in getPrimeDivisors(n):
		if i in den:
			den.remove(i)
			l.append(i)

	for i in l:
		n /= i
		d /= i

	return [n,d]

n = 1
d = 2
s = 0

while d < 1000000:
    n = 1

    while n < d:
    	if reduced(n, d) == [n, d]:
    		s += 1
    	n += 1
    d += 1

print s