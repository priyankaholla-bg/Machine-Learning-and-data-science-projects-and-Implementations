import math

def binomial_probability(n, k, p):
	if n<k:
		return -1
	def fact(n):
		if n==0:
			return 1
		else:
			return n*fact(n-1)

	comb_n_k = fact(n )/ (fact(k)*fact(n-k))
	probability = comb_n_k*(p**k)*((1-p)**(n-k))
	
	
	return round(probability, 5)
