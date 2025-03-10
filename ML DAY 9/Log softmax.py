import numpy as np

def log_softmax(scores: list) -> np.ndarray:
	exp_scores = [np.exp(score) for score in scores]
	sum_exp = sum(exp_scores)
	probabilities = [score - np.log(sum_exp) for score in scores]
	return probabilities
