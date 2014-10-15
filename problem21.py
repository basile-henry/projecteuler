def getDivs(n):

	upperLimit = n
	i = 2
	divs = [1]

	while i<upperLimit:
		if n%i == 0:
			upperLimit = n/i
			divs.append(i)
			divs.append(upperLimit)
		i+=1

	return divs

def isAmicable(n):
	return sum(getDivs(sum(getDivs(n)))) == n and n != sum(getDivs(n))

s = 0

for i in range(10000):
	if isAmicable(i):
		s+=i

print s