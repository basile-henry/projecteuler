s = 0
i = 3

while i<100000:
	part_s = 0
	for x in str(i):
		part_s+=[1, 1, 2, 6, 24, 120, 720, 5040, 40320, 362880][int(x)]
		if part_s > i:
			break
	if part_s == i:
		s+=i
		print i, s
	i+=1

print s