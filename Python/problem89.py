letters = "IVXLCDM"
values = [1,5,10,50,100,500,1000]

def fromIntToRoman(n):
	index = 6
	out = ""

	while n > 0:
		if n < values[index]:
			index -= 1
		else:
			if n/values[index-1] == 9 and letters[index-1] in "IXC":
				out += letters[index - 1] + letters[index + 1]
				index -= 1

			elif n/values[index] == 4 and letters[index] in "IXC":
				out += letters[index] + letters[index + 1]

			else:
				out += letters[index] * (n/values[index])

			n %= values[index]

	return out


def fromRomanToInt(n):
	num = 0
	index = 0

	for l in reversed(n):
		if letters.index(l) < index:
			num -= values[letters.index(l)]
		else:
			num += values[letters.index(l)]
		index = letters.index(l)

	return num


temp = open("problem89data.txt", 'r')
nums = temp.read().split('\n')
temp.close()

saved = 0

for n in nums:
	saved += len(n) - len(fromIntToRoman(fromRomanToInt(n)))

print saved