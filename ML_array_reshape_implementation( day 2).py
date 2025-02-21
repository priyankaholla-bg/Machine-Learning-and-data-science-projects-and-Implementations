import numpy as np

def reshape_matrix(a: list[list[int|float]], new_shape: tuple[int, int]) -> list[list[int|float]]:
	row=new_shape[0]
	col=new_shape[1]
	if row*col!=len(a)*len(a[0]):
		return []

	# flat_array = [element for sublist in a for element in sublist]
    
	# reshaped_matrix = [[0]*col for _ in range(row)]
	# for i in range(row):
	# 	for j in range(col):
	# 		reshaped_matrix[i][j]=flat_array[i*col+j]
	# return reshaped_matrix
	return np.array(a).reshape(new_shape).tolist()
