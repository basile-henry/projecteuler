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

def isAbundant(n):
	return sum(getDivs(n)) > n

abundants = []
numbers = range(28123)

for i in range(1,28123):
    if isAbundant(i):
    	abundants.append(i)
    	for a in abundants:
    		if (a+i) < 28123:
	    		numbers[a+i] = 0

print sum(numbers)