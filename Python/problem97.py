n = 2
for i in range(7830457-1):
	n = (n * 2) % 10000000000

print (28433 * n + 1) % 10000000000