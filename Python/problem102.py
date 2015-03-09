temp = open("problem102data.txt", 'r')
triangles = [map(int, t.split(',')) for t in temp.read().split('\n') if t != '']
temp.close()

def isInside(p1, p2, p3):
	alpha = ((p2[1] - p3[1])*(0 - p3[0]) + (p3[0] - p2[0])*(0 - p3[1])) / float((p2[1] - p3[1])*(p1[0] - p3[0]) + (p3[0] - p2[0])*(p1[1] - p3[1]))
	beta = ((p3[1] - p1[1])*(0 - p3[0]) + (p1[0] - p3[0])*(0 - p3[1])) / float((p2[1] - p3[1])*(p1[0] - p3[0]) + (p3[0] - p2[0])*(p1[1] - p3[1]))
	gamma = 1.0 - alpha - beta

	return alpha > 0 and beta > 0 and gamma > 0

count = 0

for t in triangles:
	if isInside([t[0], t[1]], [t[2], t[3]], [t[4], t[5]]):
		count+=1

print count