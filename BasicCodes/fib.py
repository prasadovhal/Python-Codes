def fib2(n):
	result = []
	a,b = 0,1
	while (a < n):
		result.append(a)
		#print(a)
		a,b = b, a+b
	return result
		
