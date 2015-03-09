from copy import copy, deepcopy

temp = open("problem81-82-83data.txt",'r')
data = [map(int, x.split(',')) for x in temp.read().split('\n') if x != '']
temp.close()

c = [deepcopy(data) for j in range(3)]

def getPath(y, x, direction):

	# caching mechanism
	if c[direction+1][y][x] != data[y][x]:
		return c[direction+1][y][x]

	ret = data[y][x]
	if x < len(data[y]) - 1:
		# reaching next column
		if direction == 0:
			# in the middle
			if y < len(data)-1 and y > 0:
				ret += min(getPath(y-1, x, -1), getPath(y+1, x, 1), getPath(y, x+1, 0))
			#bottom
			elif y == len(data)-1:
				ret += min(getPath(y-1, x, -1), getPath(y, x+1, 0))
			#top
			else:
				ret += min(getPath(y+1, x, 1), getPath(y, x+1, 0))

		# continuing upwards (negative direction)
		elif direction == -1:
			if y > 0:
				ret += min(getPath(y-1, x, -1), getPath(y, x+1, 0))
			else:
				ret += getPath(y, x+1, 0)

		# continuing downwards
		else:
			if y < len(data)-1:
				ret += min(getPath(y+1, x, 1), getPath(y, x+1, 0))
			else:
				ret += getPath(y, x+1, 0)

	c[direction+1][y][x] = ret
	return ret

#to build the ting
for i in range(len(data[0])-1,0,-1):
	for j in range(len(data)-1,-1,-1):
		getPath(j,i,0)

l = [data[i][0] + getPath(i,1,0) for i in range(len(data))]

print min(l), l
