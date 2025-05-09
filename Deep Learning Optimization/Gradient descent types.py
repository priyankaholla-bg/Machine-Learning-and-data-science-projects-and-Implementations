import numpy as np

def gradient_descent(X, y, weights, learning_rate, n_iterations, batch_size=1, method='batch'):
	
	if method=='batch':
		m = X.shape[0]
		for _ in range(n_iterations):
				y_pred = X @ weights
				errors =y_pred-y
				gradient = X.T @ errors 
				weights -= learning_rate * ((2/m) * gradient)

	elif method=='stochastic':
		for _ in range(n_iterations):
			m=1
			for i in range(X.shape[0]):
				xi = X[i].reshape(1,-1)
				yi = y[i]
				y_pred = xi @ weights
				errors = (y_pred-yi.T)
				gradient = 2/m *xi.T @ errors
				weights -= learning_rate *gradient

	elif method=='mini_batch':
		for _ in range(n_iterations):
			for start_index in range(0, X.shape[0], batch_size):
				end_index = start_index + batch_size
				xb = X[start_index:end_index]
				yb = y[start_index:end_index]
				y_pred = xb @ weights
				errors =y_pred-yb
				gradient = xb.T @ errors
				weights -= learning_rate * ( 2/len(xb) *gradient)
   
   
	return weights
