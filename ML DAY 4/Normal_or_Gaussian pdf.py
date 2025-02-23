import math

def normal_pdf(x, mean, std_dev):
    first_term = 1/(std_dev * (2*math.pi)**0.5)
    second_term = math.exp(-(x-mean)**2/(2 * std_dev**2))
    val = first_term * second_term
    return round(val,5)
