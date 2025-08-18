# ============================================
# FUNCTIONS IN PYTHON
# ============================================

# Basic Function (def with function call)

# This function prints a greeting message
def greet():
    print("Hello, welcome to Python Functions!")

# Calling the function
greet()

# This function adds two numbers and prints result
def add_numbers():
    a = 10
    b = 20
    print("The sum is:", a + b)
add_numbers()


# Function with Parameters (arguments)
# ---------------------------------------------

# Function takes 'name' as parameter and greets the person
def greet_person(name):
    print(f"Hello {name}, good morning!")
greet_person("Shahid")

# Function multiplies two numbers
def multiply(x, y):
    print("Product:", x * y)
multiply(5, 6)


# Default Parameters
# ---------------------------

# If no name is passed, default will be "Guest"
def greet_user(name="Guest"):
    
    print(f"Welcome, {name}!")

greet_user()
greet_user("Subhan")

# Calculates base^exponent
def power(base, exponent=2):
    
    print(base ** exponent)

power(5)       # default exponent = 2
power(5, 3)    # custom exponent


# Return Statement
# -------------------------

# Returns the sum of two numbers
def add(a, b):
    
    return a + b

result = add(4, 6)
print("Sum is:", result)

# Returns square of a number
def square(n):
    
    return n * n

print("Square of 7:", square(7))


# Keyword Arguments
# --------------------------

def introduce(name, age):
    print(f"My name is {name} and I am {age} years old.")

introduce(age=22, name="Ali")


def subtract(x, y):
    print("Result:", x - y)

subtract(y=10, x=25)


# Variable-length Arguments (*args, **kwargs)
# ----------------------------------------------------

# *args allows passing multiple arguments
def sum_all(*numbers):
    
    print("Sum is:", sum(numbers))

sum_all(1, 2, 3, 4, 5)

# **kwargs allows key-value arguments
def student_info(**details):
    
    for key, value in details.items():
        print(f"{key}: {value}")

student_info(name="Shahid", age=21, course="Python")


# Lambda Functions (anonymous)
# -------------------------------------

# Example 1
square = lambda x: x * x
print("Square:", square(6))

# Example 2
add = lambda a, b: a + b
print("Addition:", add(10, 20))


# Functions with Loops and Conditionals
# ----------------------------------------------

# Example 1
def even_numbers(n):
    for i in range(1, n+1):
        if i % 2 == 0:
            print(i, "is even")

even_numbers(10)

# Example 2
def factorial(n):
    result = 1
    for i in range(1, n+1):
        result *= i
    print("Factorial:", result)

factorial(5)


# Nested Functions
# -------------------------

# Example 1
def outer():
    print("Outer function")

    def inner():
        print("Inner function")
    inner()

outer()

# Example 2
def calculate(a, b):
    def add(x, y):
        return x + y
    def multiply(x, y):
        return x * y
    print("Sum:", add(a, b))
    print("Product:", multiply(a, b))

calculate(3, 4)


# Scope of Variables (local vs global)
# ----------------------------------------------

# Example 1
x = 10  # global variable

def show_global():
    print("Global x:", x)

show_global()

# Example 2
def local_scope():
    y = 20  # local variable
    print("Local y:", y)

local_scope()


# Built-in Functions (print, len, type, max, sum)
# ---------------------------------------------------------

# Example 1
numbers = [1, 2, 3, 4, 5]
print("Length:", len(numbers))
print("Type:", type(numbers))

# Example 2
print("Max:", max(numbers))
print("Sum:", sum(numbers))


# User-defined Functions
# --------------------------------

# Example 1
def say_hello():
    print("Hello from user-defined function!")

say_hello()

# Example 2
def cube(n):
    return n**3

print("Cube:", cube(3))


# Recursive Functions
# -----------------------------

# Example 1
def factorial_recursive(n):
    if n == 1:
        return 1
    return n * factorial_recursive(n-1)

print("Factorial (recursive):", factorial_recursive(5))

# Example 2
def countdown(n):
    if n == 0:
        print("Time up!")
    else:
        print(n)
        countdown(n-1)

countdown(5)


# Higher-Order Functions
# --------------------------------

# (map)
nums = [1, 2, 3, 4]
squares = list(map(lambda x: x*x, nums))
print("Squares:", squares)

# (filter)
evens = list(filter(lambda x: x % 2 == 0, nums))
print("Evens:", evens)


# Generator Functions (yield)
# -------------------------------------

# Example 1
def my_gen(n):
    for i in range(n):
        yield i

for value in my_gen(5):
    print("Generated:", value)

# Example 2
def infinite_numbers():
    n = 1
    while True:
        yield n
        n += 1

gen = infinite_numbers()
for _ in range(3):
    print(next(gen))


#  Decorators
# --------------------

# Example 1
def decorator(func):
    def wrapper():
        print("Before function")
        func()
        print("After function")
    return wrapper

@decorator
def hello():
    print("Hello from function!")

hello()

# Example 2
def uppercase_decorator(func):
    def wrapper(text):
        return func(text).upper()
    return wrapper

@uppercase_decorator
def message(text):
    return text

print(message("python is fun"))


# Methods inside Classes
# --------------------------------

class MyClass:

    # Instance Method
    def instance_method(self):
        print("This is an instance method. It uses 'self'.")

    # Class Method
    @classmethod
    def class_method(cls):
        print("This is a class method. It uses 'cls'.")

    # Static Method
    @staticmethod
    def static_method():
        print("This is a static method. It does not use self or cls.")


# Example 1
obj = MyClass()
obj.instance_method()
MyClass.class_method()
MyClass.static_method()

# Example 2
class Calculator:
    def __init__(self, num):
        self.num = num

    def double(self):
        # Instance method
        return self.num * 2

    @classmethod
    def add(cls, a, b):
        # Class method
        return a + b

    @staticmethod
    def greet():
        # Static method
        print("Hello from Calculator class!")

calc = Calculator(10)
print("Double:", calc.double())
print("Sum:", Calculator.add(5, 7))
Calculator.greet()
