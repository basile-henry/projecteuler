temp = open("problem18data.txt", 'r')
data = [map(int, a.split(' ')) for a in temp.read().split('\n')]
temp.close()

def getMaxSum(depth, index):
	if depth == len(data)-1:
		if index == len(data[depth]) - 1:
			return data[depth][index]
		return max(data[depth][index], data[depth][index+1])
	return data[depth][index] + max(getMaxSum(depth+1, index), getMaxSum(depth+1, index+1))

print getMaxSum(0,0)