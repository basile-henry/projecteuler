def isPal(n):
	return "".join(reversed(str(n))) == str(n)

def toBinary(n):
	return "{0:b}".format(n)

s = 0
for i in range(1000000):
	if isPal(i) and isPal(toBinary(i)):
		s+=i

print s