import math
def add(a, b):

    return a + b

def subtract(a, b):
    
    return a - b

def multiply(a, b):
    
    return a * b

def divide(a, b):
    if b == 0:
        return "Error: Division by zero is not allowed."
    return a / b

def factorial(n):
    return math.factorial(n)

def power(a, b):
    return math.pow(a, b)