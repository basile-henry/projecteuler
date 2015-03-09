def getProduct(n):
	n = str(n)
	for a in range(1, len(n) - 2):
		for b in range(a+1, len(n) - 1):
			if int(n[:a]) * int(n[a:b]) == int(n[b:]):
				return int(n[b:])

	return 0

l = range(1, 10)
p = []

for a in l:
	for b in l:
		if b != a:
			for c in l:
				if c != a and c != b:
					for d in l:
						if d != a and d != b and d != c:
							for e in l:
								if e != a and e != b and e != c and e != d:
									for f in l:
										if f != a and f != b and f != c and f != d and f != e:
											for g in l:
												if g != a and g != b and g != c and g != d and g != e and g != f:
													for h in l:
														if h != a and h != b and h != c and h != d and h != e and h != f and h != g:
															for i in l:
																if i != a and i != b and i != c and i != d and i != e and i != f and i != g and i != h:
																	p.append(getProduct(''.join(map(str, [a,b,c,d,e,f,g,h,i]))))

print sum(list(set(p)))