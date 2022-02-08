import random

def quadraticEquation():
    alpha= random.randint(1, 20)
    beta= random.randint(1, 20)
    equation_string= f"x^2 +{alpha+ beta}x + {alpha* beta} = 0"
    return equation_string
