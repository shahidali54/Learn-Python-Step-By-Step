# Ye hamara custom module hai jisme kuch functions aur constants define kiye gaye hain

PI = 3.14159

def add(a, b):
    """Return the sum of two numbers"""
    return a + b

def subtract(a, b):
    """Return the difference of two numbers"""
    return a - b

def multiply(a, b):
    """Return the product of two numbers"""
    return a * b

def divide(a, b):
    """Return the division of two numbers (handles divide by zero)"""
    if b == 0:
        return "Error! Division by zero."
    return a / b
