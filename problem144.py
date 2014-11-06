from math import *

def  quadratic(a, b, c):
	delta = sqrt(b**2-4*a*c)

	return [-b+delta/(2*float(a)), -b-delta/(2*float(a))]


def intersection(m, p):
	x = quadratic(4+m**2, 2*m*p, p**2-100)
	y = quadratic(4/float(m**2) + 1, -8*p/float(m**2), 4*p**2/float(m**2) - 100)

	return zip(x,y)

print intersection(-19.7/1.4,10.1)