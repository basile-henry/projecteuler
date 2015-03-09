def isAsc(n):
	n = str(n)
	for i in range(len(n)-1):
		if int(n[i]) > int(n[i+1]):
			return False
	return True

def isDesc(n):
	n = str(n)
	for i in range(len(n)-1):
		if int(n[i]) < int(n[i+1]):
			return False
	return True

s = 0
i = 100

while (s / float(i) < 0.99):
	i+=1
	if not isDesc(i) and not isAsc(i):
		s+=1

print s, i