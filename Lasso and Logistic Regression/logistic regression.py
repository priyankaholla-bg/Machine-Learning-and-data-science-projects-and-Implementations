import numpy as np

def predict_logistic(X: np.ndarray, weights: np.ndarray, bias: float) -> np.ndarray:
	"""
	Implements binary classification prediction using Logistic Regression.

	Args:
		X: Input feature matrix (shape: N x D)
		weights: Model weights (shape: D)
		bias: Model bias

	Returns:
		Binary predictions (0 or 1)
	"""
	def sigmoid(x):
		return 1 / (1 + np.exp(-x))
	
	y_pred = X @ weights + bias
	y_pred = sigmoid(y_pred)
	y_pred_outputs = (y_pred >= 0.5).astype(int)

	return y_pred_outputs
	

