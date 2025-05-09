def matrix_dot_vector(a:list[list[int|float]],b:list[int|float])-> list[int|float]:
	if len(a[0])!=len(b):
		return -1
	c=[]
	for mat in a:
		sum=0
		for i in range(len(b)):
			sum+=(mat[i]*b[i])
		c.append(sum)
	return c
