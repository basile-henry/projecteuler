temp = open("problem107data.txt", 'r')
data = [d.split(',') for d in temp.read().split('\n') if d != ""]
temp.close()

def getWeight():
	return sum([sum([int(d) for d in l if d != '-']) for l in data])/2

initial_weight = getWeight()


