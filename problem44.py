def getPent(n):
	return n*(3*n-1)/2

def mainLoop():
	pents = []

	for i in range(1,20000):
		pents.append(getPent(i))

	for i in range(1,len(pents)-500):
		for j in range(1,500):
			if (pents[i + j] - pents[i]) in pents:
				if (pents[i + j] + pents[i]) in pents:
					print pents[i], pents[i+j], pents[i+j]-pents[i]
					return
		
		if i%100 == 0:
			print i

mainLoop()