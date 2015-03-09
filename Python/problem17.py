count = len("onethousand")

units = map(len,['one','two','three','four','five','six','seven','eight','nine'])

def getLength(n):
	if n == 0:
		return 0
	if n < 10:
		return units[n-1] 
	if n < 20:
		return len(['ten','eleven','twelve','thirteen','fourteen','fifteen','sixteen','seventeen','eighteen','nineteen'][n-10])
	if n < 100 and n%10!=0:
		return len(['twenty','thirty','forty','fifty','sixty','seventy','eighty','ninety'][(n/10)-2]) + units[n%10-1]
	if n < 100:
		return len(['twenty','thirty','forty','fifty','sixty','seventy','eighty','ninety'][(n/10)-2])
	if n%100 == 0:
		return units[n/100-1] + len("hundred")
	return units[n/100-1] + len("hundredand") + getLength(n%100)

for i in range(1,1000):
	count+= getLength(i)

print count