# =========================================
#  Variables in Python
# =========================================

# =========================================
# first program
# =========================================
print("Hello, World!")

# -----------------------------
# Creating simple variables
# -----------------------------
name = "Shahid"  # A string variable storing a name
age = 25         # An integer variable storing age
height = 5.9     # A float variable storing height in feet
is_student = True  # A boolean variable

print(name, age, height, is_student)

# -----------------------------
# Multiple assignments in one line
# -----------------------------
x, y, z = 10, 20, 30  # Assigning values to multiple variables in a single line
print(x, y, z)

# -----------------------------
# Assigning the same value to multiple variables
# -----------------------------
a = b = c = 100  # All three variables store the same value
print(a, b, c)

# -----------------------------
# Changing the value of a variable (Variable Overwriting)
# -----------------------------
message = "Hello"
print(message)
message = "Welcome"  # Now 'message' variable stores a different value
print(message)

# -----------------------------
# Checking variable data type
# -----------------------------
num = 50
print(type(num))  # <class 'int'>

text = "Python"
print(type(text))  # <class 'str'>

# -----------------------------
# Constants in Python (by convention)
# -----------------------------
PI = 3.1416  # Constants are usually written in UPPERCASE
GRAVITY = 9.8
print(PI, GRAVITY)

# Note: Python does not have true constants, 
# so these values can still be changed, but by convention we don't change them.

# -----------------------------
# Dynamic typing in Python
# -----------------------------
value = 10         # Initially an integer
print(value, type(value))
value = "Ten"      # Now the same variable stores a string
print(value, type(value))

# -----------------------------
# Variable naming rules
# -----------------------------
# ✅ Valid variable names
my_var = 5
_var = "Valid"
var123 = 10

# ❌ Invalid variable names (These will cause errors if uncommented)
# 123var = 10
# my-var = 20
# class = "Hello"

# -----------------------------
# Deleting a variable
# -----------------------------
temp = 100
print(temp)
del temp  # Deletes the variable from memory
# print(temp)  # This will cause an error because 'temp' no longer exists
