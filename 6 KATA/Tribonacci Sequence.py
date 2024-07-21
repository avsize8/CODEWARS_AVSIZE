def tribonacci(signature, n):
	tribo = []
	if n > 0 and n < 3:
		for i in range(n):
			tribo.append(signature[i])
	elif n >= 3:
		tribo = signature
	
	for i in range(n-3):
		sum = tribo[i] + tribo[i+1] + tribo[i+2]
		tribo.append(sum)
	
	return tribo