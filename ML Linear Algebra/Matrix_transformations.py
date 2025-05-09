import numpy as np

def transform_matrix(A: list[list[int|float]], T: list[list[int|float]], S: list[list[int|float]]) -> list[list[int|float]]:
	if T[0][0]*T[1][1] - T[0][1]*T[1][0]==0:
		return -1
	if S[0][0]*S[1][1] - S[0][1]*S[1][0]==0:
		return -1
    
	# T_inv = [[0]*2 for _ in range(2)]

	# det_T = T[0][0]*T[1][1] - T[0][1]*T[1][0]
	# T_inv = np.array([[0, 0], [0, 0]])
	# T_inv[0][0] = T[1][1] / det_T
	# T_inv[1][1] = T[0][0] / det_T
	# T_inv[1][0] = -T[1][0] / det_T
	# T_inv[0][1] = -T[0][1] / det_T

	T_inv = np.linalg.inv(T)
	result = (T_inv @ A) @ S
	return result.tolist()

def inverse_2x2(matrix: list[list[float]]) -> list[list[float]]:
	if matrix[0][0]*matrix[1][1] - matrix[0][1]*matrix[1][0]==0:
		return -1

	matrix_inv = [[0]*2 for _ in range(2)]

	matrix_det = matrix[0][0]*matrix[1][1] - matrix[0][1]*matrix[1][0]
	matrix_inv[0][0] = matrix[1][1] / matrix_det
	matrix_inv[1][1] = matrix[0][0] / matrix_det
	matrix_inv[0][1] = -matrix[0][1] / matrix_det
	matrix_inv[1][0] = -matrix[1][0] / matrix_det
	
	return matrix_inv
