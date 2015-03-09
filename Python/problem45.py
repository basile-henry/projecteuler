def getT(n):
	return n*(n+1)/2

def getP(n):
	return n*(3*n-1)/2

def getH(n):
	return n*(2*n-1)

t = []
p = []
h = []

for i in range(1,100000):
	t.append(getT(i))
	p.append(getP(i))
	h.append(getH(i))

m = 0
mp = 0
mh = 0
for tt in range(99999):
	for pp in range(mp,99999):
		if t[tt] == p[pp]:
			for hh in range(mh,99999):
				if t[tt] == p[pp] and t[tt] == h[hh]:
					m = t[tt]
				if t[tt] < h[hh]:
					mh=0
					break
		if t[tt] < p[pp]:
			mp = pp
			break
	print tt, m