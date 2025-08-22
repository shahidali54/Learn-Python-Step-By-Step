# Is file me hum 2 built-in modules cover karenge:
# 1. itertools → advanced iteration tools
# 2. functools → functional programming utilities

import itertools
import functools

print("========== ITERTOOLS Module ==========\n")

# count() → infinite counting (we limit with islice)
counter = itertools.count(start=1, step=2)   # odd numbers
print("Count first 5 odd numbers:", list(itertools.islice(counter, 5)))

# cycle() → repeat sequence infinitely
colors = ["red", "green", "blue"]
cycled = itertools.cycle(colors)
print("Cycle first 6 values:", [next(cycled) for _ in range(6)])

# combinations() → all possible pairs
letters = ["A", "B", "C"]
print("Combinations of 2 letters:", list(itertools.combinations(letters, 2)))

# groupby() → group consecutive elements
animals = ["cat", "cat", "dog", "dog", "dog", "bird"]
for key, group in itertools.groupby(animals):
    print("Group:", key, "->", list(group))


print("\n========== FUNCTOOLS Module ==========\n")

# reduce() → apply a function cumulatively
numbers = [1, 2, 3, 4]
product = functools.reduce(lambda x, y: x * y, numbers)
print("Reduce product of list:", product)

# partial() → fix arguments of a function
def power(base, exp):
    return base ** exp

square = functools.partial(power, exp=2)  # always square
print("Partial square(5):", square(5))

# lru_cache() → cache results of expensive function
@functools.lru_cache(maxsize=None)
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

print("Fibonacci(10) with caching:", fibonacci(10))

# total_ordering → automatic comparison methods
@functools.total_ordering
class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
    
    def __eq__(self, other):
        return self.marks == other.marks
    
    def __lt__(self, other):
        return self.marks < other.marks

s1 = Student("Shahid", 85)
s2 = Student("Subhan", 90)
print("Is Shahid < Subhan?", s1 < s2)
print("Is Shahid <= Subhan?", s1 <= s2)
