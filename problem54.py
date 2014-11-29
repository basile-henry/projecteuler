temp = open("problem54data.txt", 'r')
hands = [[[c for c in m[:14].split(' ')], [c for c in m[15:].split(' ')]] for m in temp.read().split('\n') if m != '']
temp.close()

def highCard(h):
	m = 0

	for c in h:
		if 'A' == c[0]:
			return 13
		elif 'K' == c[0]:
			m = max(m, 12)
		elif 'Q' == c[0]:
			m = max(m, 11)
		elif 'J' == c[0]:
			m = max(m, 10)
		elif 'T' == c[0]:
			m = max(m, 9)
		else:
			m = max(m, int(c[0]))

	return m

def onePair(h):
	h = [c[0] for c in h]

	for i in range(len(h)):
		t = h[:]
		c = t.pop(i)
		if c in t:
			return highCard([c])

	return 0


def twoPair(h):
	h = [c[0] for c in h]

	for i in range(len(h)):
		t = h[:]
		c = t.pop(i)
		if c in t and onePair(t) != 0:
			return max(highCard([c]), onePair(t))

	return 0


def three(h):
	h = [c[0] for c in h]

	for i in range(len(h)):
		t = h[:]
		c = t.pop(i)
		if highCard([c]) == onePair(t):
			return highCard([c])

	return 0

# def straight(h):


# def flush(h):


# def full(h):


# def four(h):


# def straightFlush(h):
# 	if flush(h) != 0 and straight(h) != 0:
# 		return straight(h)

print full(['TH', '8H', '5C', 'QS', 'TC'])