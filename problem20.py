fac = 1

for i in range(1,101):
	fac*=i

print sum(map(int, str(fac)))