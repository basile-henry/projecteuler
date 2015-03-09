temp = open("problem67data.txt", 'r')
data = [map(int, x.split(' ')) for x in temp.read().split('\n')]
temp.close()

for i in range(len(data)-2, -1, -1):
	for j in range(len(data[i])):
		data[i][j] += max(data[i+1][j], data[i+1][j+1])

print data[0][0]