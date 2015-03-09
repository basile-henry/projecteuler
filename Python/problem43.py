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

s = 0
for p in getPans(range(0,10)):
	if int(p[1:4])%2 == 0 and int(p[2:5])%3 == 0 and int(p[3:6])%5 == 0 and int(p[4:7])%7 == 0 and int(p[5:8])%11 == 0 and int(p[6:9])%13 == 0 and int(p[7:10])%17 == 0:
		s+=int(p)
		print p

print "Sum:", s