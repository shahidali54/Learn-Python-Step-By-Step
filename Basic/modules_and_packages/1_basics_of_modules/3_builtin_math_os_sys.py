# Ye file Python ke kuch built-in modules ka demo hai:
# - math
# - os
# - sys

import math
import os
import sys


print("---- Using math module ----")
# Square root and factorial
print("Square root of 16:", math.sqrt(16))
print("Factorial of 5:", math.factorial(5))

# Trigonometric functions
print("Cosine of 0:", math.cos(0))
print("Pi value from math module:", math.pi)


print("\n---- Using os module ----")
# Get current working directory
print("Current Working Directory:", os.getcwd())

# List all files in current directory
print("Files in current directory:", os.listdir("."))


print("\n---- Using sys module ----")
# Python version
print("Python Version:", sys.version)

# Command line arguments
print("Command Line Arguments:", sys.argv)  # argv[0] is always the script name
