def calculate_matrix_mean(matrix: list[list[float]], mode: str) -> list[float]:
	means=[]
	if mode=='column':
		for mat in zip(*(matrix)):
			mean=0
			for i in mat:
				mean += i
			means.append(mean/len(mat))
	elif mode=='row':
		for mat in matrix:
			mean=0
			for ele in mat:
				mean +=ele
			means.append(mean/len(mat))

	return means
