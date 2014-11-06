a = "0123456789"

def fac(n):
	if n==1:
		return 1
	return n*fac(n-1)

n = 10
m = 1000000
s = 0

while n>1:
	if (s+1)*fac(n) >= m:
		print s
		m-=s*fac(n)
		n-=1
		s = -1
	s+=1


print "m:", m



16728043