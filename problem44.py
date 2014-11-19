pents = []

def getPent(n):
	return n*(3*n-1)/2

def check():
	for top in reversed(pents):
		for bottom in pents:
			if top + bottom == pents[-1]:
				if top - bottom in pents:
					print top - bottom
					return False
			if bottom == top:
				break

	return True

i = 0

while check():
	i+=1
	pents.append(getPent(i))