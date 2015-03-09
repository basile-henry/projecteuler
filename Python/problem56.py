max = 0
for a in range(101):
	for b in range(101):
		s = sum(map(int,str(a**b)))
		if s > max:
			max = s

print max
