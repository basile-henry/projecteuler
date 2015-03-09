temp = open("problem42words.txt", 'r')
words = temp.read().replace("\"","").split(",")
temp.close()

def value(w):
	return sum([ord(l) - ord('A') + 1 for l in w])

def getTriangleNumber(n):
	return n*(n+1)/2

def isTriangleWord(w):
	v = value(w)
	i = 1

	while getTriangleNumber(i) < v:
		i += 1

	return getTriangleNumber(i) == v

count = 0

for w in words:
	if isTriangleWord(w):
		count += 1

print count