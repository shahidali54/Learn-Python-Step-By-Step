# Yahan hum apna custom module (math_utils.py) import karke use karenge

# ✅ Import full module
import math_utils

# ✅ Import specific function
from math_utils import add, PI


print("---- Using Custom Module ----")

# Full module ka use
print("Addition (using full module):", math_utils.add(10, 5))
print("Subtraction:", math_utils.subtract(10, 5))
print("Multiplication:", math_utils.multiply(10, 5))
print("Division:", math_utils.divide(10, 0))  # handle divide by zero

# Specific import ka use
print("Addition (using direct import):", add(20, 30))
print("Value of PI:", PI)
