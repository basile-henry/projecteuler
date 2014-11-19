def isPan(a, b):
	return set(str(a)) == set(str(b)) and len(str(a)) == len(str(b))

i = 1

while True:

	if all([isPan(i, i*x) for x in range(2,7)]):
		print i
		break

	i+=1
	