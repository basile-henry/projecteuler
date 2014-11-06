import math

temp = open("problem102data.txt", 'r')
triangles = [map(int, t.split(',')) for t in temp.read().split('\n') if t != '']
temp.close()

def diff(a, b):
	diff = a - b
	if diff < -math.pi:
		return diff + 2*math.pi
	if diff > math.pi:
		return diff - 2*math.pi
	return diff

s = 0
for t in triangles:
	angles = [math.atan2(t[1], t[0]), math.atan2(t[3], t[2]), math.atan2(t[5], t[4])]

	if abs(diff(t[0],t[1])) >= math.pi or abs(diff(t[1],t[2])) >= math.pi or abs(diff(t[0],t[2])) >= math.pi:
		s+=1
		print s