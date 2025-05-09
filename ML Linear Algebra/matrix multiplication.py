def matrixmul(a:list[list[int|float]],
              b:list[list[int|float]])-> list[list[int|float]]:
	
	if len(a[0])!=len(b):
		return -1
    
	c = [[0 for _ in range(len(b[0]))] for _ in range(len(a))]
	for i in range(len(a)):
		for j in range(len(b[0])):
			for k in range(len(b)):
				c[i][j] += a[i][k] * b[k][j]

	return c
	
	# return [[sum(x*y for x,y in zip(A_row, B_col)) for B_col in zip(*b)] for A_row in a]
