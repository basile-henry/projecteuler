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

def reduce(n,d):
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

n = 2
d = 7
m = float(2)/7
t = float(3)/7


while d < 1000000:

	q = float(n)/d

	if q >= t:
		d += 1
	elif q > m:
		m = q
		best_n = n
		best_d = d
		n += 1
	else:
		n += 1

print best_n, best_d, reduce(best_n, best_d)
