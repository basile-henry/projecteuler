coins = [1,2,5,10,20,50,100,200]

def c(n,x):
	if n < 0:
		return 0
	if x == 0:
		return 1
	return c(n-coins[x],x) + c(n,x-1)

print c(200,7)