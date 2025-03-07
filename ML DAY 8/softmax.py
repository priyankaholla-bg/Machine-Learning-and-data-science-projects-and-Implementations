import math

def softmax(scores: list[float]) -> list[float]:
	exp_scores = [math.exp(score) for score in scores]
	sum_exp_scores = sum(exp_scores)
	probabilities = [math.exp(score)/sum_exp_scores for score in scores]
	return probabilities
