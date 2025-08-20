# ====================================
# Python Loops
# ====================================

# 1. TYPES OF LOOPS
# ----------------

# For loop with a list
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print("For loop list item:", fruit)

# For loop with a string
for char in "Hello":
    print("For loop string char:", char)

# For loop with a tuple
numbers = (1, 2, 3)
for n in numbers:
    print("For loop tuple item:", n)

# For loop with range
for i in range(3):
    print("For loop range item:", i)

# While loop
count = 0
while count < 3:
    print("While loop count:", count)
    count += 1


# 2. LOOP CONTROL STATEMENTS
# --------------------------

# Break
for i in range(5):
    if i == 3:
        print("Break at:", i)
        break
    print("Loop value:", i)

# Continue
for i in range(5):
    if i == 2:
        print("Skipping:", i)
        continue
    print("Loop value:", i)

# Pass
for i in range(3):
    if i == 1:
        pass  # Does nothing
    print("Pass example value:", i)


# 3. LOOP WITH ELSE
# -----------------

# for…else
for i in range(3):
    print("For loop value:", i)
else:
    print("For loop completed without break")

# While…else
count = 0
while count < 3:
    print("While loop value:", count)
    count += 1
else:
    print("While loop completed without break")


# 4. NESTED LOOPS
# ----------------

# For inside for
for i in range(2):
    for j in range(2):
        print(f"Nested for: i={i}, j={j}")

# While inside for
for i in range(2):
    j = 0
    while j < 2:
        print(f"For-While nested: i={i}, j={j}")
        j += 1


# 5. RANGE() FUNCTION WITH LOOPS
# ------------------------------

# Simple range
for i in range(5):
    print("Range simple:", i)

# Range with step
for i in range(2, 10, 2):
    print("Range with step:", i)


# 6. ITERATING DIFFERENT DATA STRUCTURES
# --------------------------------------

# Loop with string
for char in "Python":
    print("String char:", char)

# Loop with list
for item in [10, 20, 30]:
    print("List item:", item)

# Loop with tuple
for t in (100, 200):
    print("Tuple item:", t)

# Loop with set
for s in {"A", "B", "C"}:
    print("Set item:", s)

# Loop with dictionary
person = {"name": "Shahid", "age": 25}
for key, value in person.items():
    print("Dict key:", key, "| Value:", value)

# Loop with enumerate()
names = ["Shahid", "Subhan", "Dilbar"]
for index, name in enumerate(names):
    print(f"Index {index} -> Name {name}")

# Loop with zip()
roll_numbers = [1, 2, 3]
students = ["Shahid", "Subhan", "Dilbar"]
for r, s in zip(roll_numbers, students):
    print(f"Roll {r} -> Student {s}")


# 7. COMPREHENSIONS (SHORTCUT LOOPS)
# ----------------------------------

# List comprehension
squares = [x**2 for x in range(5)]
print("List comprehension (squares):", squares)

# Dictionary comprehension
squares_dict = {x: x**2 for x in range(5)}
print("Dictionary comprehension:", squares_dict)

# Set comprehension
unique_numbers = {x % 3 for x in range(10)}
print("Set comprehension:", unique_numbers)

# Generator comprehension
gen = (x**2 for x in range(5))
print("Generator comprehension values:")
for value in gen:
    print(value)

