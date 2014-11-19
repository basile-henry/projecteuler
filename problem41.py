def getPans(l):
	if len(l) == 1:
		return [str(l[0])]

	ret = []
	for x in l:
		p = l[:]
		p.remove(x)
		for y in getPans(p):
			ret.append(str(x) + y)

	return ret

print getPans(range(0,10))[999999]