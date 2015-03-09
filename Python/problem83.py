temp = open("problem81-82-83data.txt",'r')
data = [map(int, x.split(',')) for x in temp.read().split('\n') if x != '']
temp.close()

cache = [[[0 for x in y] for y in data] for j in range(4)]

def shortPath(a, b, direction):
	if direction == 0:
		a = max(0, a - 1)
	if direction == 1:
		b += 1
	if direction == 2:
		a += 1
	if direction == 3:
		b = max(0, b - 1)


	if a == len(data)-1 and b == len(data[0])-1:
		return data[a][b]

	if cache[direction][a][b] != 0:
		return cache[direction][a][b]

	# Up == 0
	if direction == 0:
		if a == len(data)-1 and b:
			cache[direction][a][b] = data[a][b] + min(shortPath(a, b+1, 1), shortPath(a, b-1, 3))

		elif b == len(data[0])-1:
			cache[direction][a][b] = data[a][b] + min(shortPath(a-1, b, 0), shortPath(a, b-1, 3))

		else:
			cache[direction][a][b] = data[a][b] + min(shortPath(a-1, b, 0), shortPath(a, b+1, 1), shortPath(a, b-1, 3))



	return cache[direction][a][b]


print shortPath(0,0)