import math

def poisson_probability(k, lam):
	def factorial(n):
		if n==0:
			return 1
		else:
			return n*factorial(n-1)
	
	
	val = math.exp(-lam)*(lam**k)/factorial(k)
	return round(val,5)
