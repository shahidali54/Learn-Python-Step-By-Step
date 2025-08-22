# Ye file Python ke kuch built-in modules ka demo hai:
# - random
# - datetime

import random
import datetime


print("---- Using random module ----")
# Generate random numbers
print("Random integer between 1 and 10:", random.randint(1, 10))
print("Random float between 0 and 1:", random.random())

# Random choice and shuffle
fruits = ["apple", "banana", "cherry", "mango"]
print("Random fruit choice:", random.choice(fruits))

random.shuffle(fruits)
print("Shuffled fruits list:", fruits)


print("\n---- Using datetime module ----")
# Current date and time
current_time = datetime.datetime.now()
print("Current date and time:", current_time)

# Formatting dates
print("Formatted date:", current_time.strftime("%d-%m-%Y"))
print("Formatted time:", current_time.strftime("%H:%M:%S"))
