def transpose_matrix(a: list[list[int|float]]) -> list[list[int|float]]:
	# col=len(a[0])
	# row=len(a)
	# b = [[0]*row for _ in range(col)]
	# for i in range(row):
	# 	for j in range(col):
	# 		b[j][i]=a[i][j]
	# return b

	return [list(i) for i in zip(*(a))]
