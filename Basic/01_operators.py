# =========================
# Python Operators 
# =========================

# --------- 1. Arithmetic Operators ---------
print("\n--- Arithmetic Operators ---")

a = 10
b = 3

# Addition
print("Addition (+):", a + b)        # Adds two numbers (10 + 3 = 13)
# Subtraction
print("Subtraction (-):", a - b)     # Subtracts two numbers (10 - 3 = 7)
# Multiplication
print("Multiplication (*):", a * b)  # Multiplies two numbers (10 * 3 = 30)
# Division
print("Division (/):", a / b)        # Divides and returns float result (10 / 3 = 3.333...)
# Floor Division
print("Floor Division (//):", a // b) # Divides and returns integer result (10 // 3 = 3)
# Modulus
print("Modulus (%):", a % b)         # Returns remainder (10 % 3 = 1)
# Exponentiation
print("Exponentiation (**):", a ** b) # Power calculation (10 ** 3 = 1000)


# --------- 2. Assignment Operators ---------
print("\n--- Assignment Operators ---")

x = 5
print("Initial value of x:", x)

x += 3   # Add and assign
print("After x += 3:", x)

x -= 2   # Subtract and assign
print("After x -= 2:", x)

x *= 4   # Multiply and assign
print("After x *= 4:", x)

x /= 3   # Divide and assign
print("After x /= 3:", x)

x //= 2  # Floor divide and assign
print("After x //= 2:", x)

x %= 3   # Modulus and assign
print("After x %= 3:", x)

x **= 2  # Power and assign
print("After x **= 2:", x)

# Convert float to integer before bitwise operations
x = int(x)

x &= 1   # Bitwise AND and assign
print("After x &= 1:", x)

x |= 2   # Bitwise OR and assign
print("After x |= 2:", x)

x ^= 3   # Bitwise XOR and assign
print("After x ^= 3:", x)

x >>= 1  # Right shift and assign
print("After x >>= 1:", x)

x <<= 2  # Left shift and assign
print("After x <<= 2:", x)


# --------- 3. Comparison Operators ---------
print("\n--- Comparison Operators ---")

p = 7
q = 10

print("p == q:", p == q)   # Equal to
print("p != q:", p != q)   # Not equal to
print("p > q:", p > q)     # Greater than
print("p < q:", p < q)     # Less than
print("p >= q:", p >= q)   # Greater than or equal to
print("p <= q:", p <= q)   # Less than or equal to


# --------- 4. Logical Operators ---------
print("\n--- Logical Operators ---")

a = True
b = False

print("a and b:", a and b) # Returns True if both are True
print("a or b:", a or b)   # Returns True if at least one is True
print("not a:", not a)     # Reverses the boolean value


# --------- 5. Bitwise Operators ---------
print("\n--- Bitwise Operators ---")

m = 6   # binary: 110
n = 3   # binary: 011

print("m & n:", m & n)     # Bitwise AND
print("m | n:", m | n)     # Bitwise OR
print("m ^ n:", m ^ n)     # Bitwise XOR
print("~m:", ~m)           # Bitwise NOT
print("m << 1:", m << 1)   # Left shift
print("m >> 1:", m >> 1)   # Right shift


# --------- 6. Membership Operators ---------
print("\n--- Membership Operators ---")

numbers = [1, 2, 3, 4, 5]

print("3 in numbers:", 3 in numbers)       # Checks if 3 exists in the list
print("10 in numbers:", 10 in numbers)     # Checks if 10 exists in the list
print("7 not in numbers:", 7 not in numbers) # Checks if 7 is not in the list


# --------- 7. Identity Operators ---------
print("\n--- Identity Operators ---")

list1 = [1, 2, 3]
list2 = [1, 2, 3]
list3 = list1

print("list1 is list2:", list1 is list2)       # False, different objects with same content
print("list1 is list3:", list1 is list3)       # True, same object reference
print("list1 is not list2:", list1 is not list2) # True, different objects