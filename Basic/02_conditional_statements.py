# ---Simple if statement ---
age = 20
if age >= 18:  # condition check
    print("You are an adult")  
# Output: You are an adult


# ---if-else statement ---
age = 15
if age >= 18:
    print("You are an adult")
else:
    print("You are a minor")
# Output: You are a minor


# ---if-elif-else ---
marks = 75
if marks >= 90:
    print("Grade A")
elif marks >= 70:
    print("Grade B")
elif marks >= 50:
    print("Grade C")
else:
    print("Fail")
# Output: Grade B


# ---Nested if ---
num = 10
if num > 0:
    if num % 2 == 0:
        print("Positive Even number")
    else:
        print("Positive Odd number")
# Output: Positive Even number


# ---Multiple conditions using and ---
x = 25
if x > 10 and x < 50:
    print("x is between 10 and 50")
# Output: x is between 10 and 50


# ---Multiple conditions using or ---
city = "Karachi"
if city == "Lahore" or city == "Karachi":
    print("City is in Pakistan")
# Output: City is in Pakistan


# ---Using not ---
is_raining = False
if not is_raining:
    print("You can go outside, no rain!")
# Output: You can go outside, no rain!


# ---Checking membership ---
fruits = ["apple", "banana", "mango"]
if "apple" in fruits:
    print("Apple is available in fruits list")
# Output: Apple is available in fruits list


# ---Comparing strings ---
password = "admin123"
if password == "admin123":
    print("Correct password")
else:
    print("Wrong password")
# Output: Correct password


# ---Short-hand if-else (Ternary Operator) ---
num = 7
print("10:", "Even" if num % 2 == 0 else "Odd")
# Output: 10: Odd