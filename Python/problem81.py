temp = open("problem81-82-83data.txt",'r')
data = [map(int, x.split(',')) for x in temp.read().split('\n') if x != '']
temp.close()

cache = [[0 for x in y] for y in data]

def shortPath(a,b):
	if a == len(data)-1 and b == len(data[0])-1:
		return data[a][b]

	if cache[a][b] != 0:
		return cache[a][b]

	if a == len(data)-1:
		cache[a][b] = data[a][b] + shortPath(a, b+1)
		return cache[a][b]

	if b == len(data[0])-1:
		cache[a][b] = data[a][b] + shortPath(a+1, b)
		return cache[a][b]

	cache[a][b] = data[a][b] + min(shortPath(a+1, b), shortPath(a, b+1))
	return cache[a][b]


print shortPath(0,0)