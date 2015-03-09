def howManyIn(size, m):
	return 1 + sum([howManyIn(size, m-i) for i in range(1, size) if m-i-1 > 0])

for i in range(1, 10):
	print i, howManyIn(i, i)

# p(1) = 1
# p(2) = 2
# p(3) = 3
# p(4) = 4
# p(5) = 7