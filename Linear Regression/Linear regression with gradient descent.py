import numpy as np
def linear_regression_gradient_descent(X: np.ndarray, y: np.ndarray, alpha: float, iterations: int) -> np.ndarray:
	# Your code here, make sure to round
	m, n = X.shape
	theta = np.zeros((n, 1))
	for _ in range(iterations):
		pred = X @ theta
		errors = pred-y.reshape(-1,1)
		update = X.T @ errors /m
		theta-= alpha * update

	return np.round(theta.flatten() , 4)
