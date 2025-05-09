import numpy as np

def l1_regularization_gradient_descent(X: np.array, y: np.array, alpha: float = 0.1, learning_rate: float = 0.01, max_iter: int = 1000, tol: float = 1e-4) -> tuple:
	n_samples, n_features = X.shape

	weights = np.zeros(n_features)
	bias = 0
	for _ in range(max_iter):
		y_pred = X @ weights + bias
		error = y_pred - y
		gradient_w = X.T @ error * (1/n_samples) + alpha * np.sign(weights)
		gradient_b = np.sum(error) * (1/n_samples)

		weights = weights - learning_rate * gradient_w
		bias = bias -  learning_rate * gradient_b

	return (weights, bias)
