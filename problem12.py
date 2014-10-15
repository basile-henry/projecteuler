def getDivs(n):

	upperLimit = n
	i = 2
	divs = [1]

	while i<upperLimit:
		if n%i == 0:
			upperLimit = n/i
			divs.append(i)
			if i != upperLimit:
				divs.append(upperLimit)
		i+=1

	return divs

i = 2
t = 1

while len(getDivs(t))+1<500:
	t += i
	i += 1
	
	print t
