import math

sqrt_64 = math.sqrt(64)
print("Square root of 64:", sqrt_64)

pi_value = math.pi
e_value = math.e
print("Value of pi:", pi_value)
print("Value of e:", e_value)

sine_90 = math.sin(math.radians(90))
cosine_90 = math.cos(math.radians(90))
print("Sine of 90 degrees:", sine_90)
print("Cosine of 90 degrees:", cosine_90)

rounded_value = round(15.6789, 2)
print("15.6789 rounded to 2 decimal places:", rounded_value)

import os

cwd = os.getcwd()
print("Current working directory:", cwd)

try:
    os.mkdir("Assignment")
    print("Directory 'Assignment' created.")
except FileExistsError:
    print("Directory 'Assignment' already exists.")

entries = os.listdir(cwd)
print("Files and directories in the current working directory:", entries)

try:
    os.rmdir("Assignment")
    print("Directory 'Assignment' deleted.")
except FileNotFoundError:
    print("Directory 'Assignment' does not exist.")
except OSError:
    print("Directory 'Assignment' is not empty or cannot be deleted.")

import random

random_number = random.randint(1, 100)
print("Random number between 1 and 100:", random_number)

items = ['apple', 'banana', 'cherry', 'date']
random_item = random.choice(items)
print("Randomly selected item:", random_item)

numbers = [1, 2, 3, 4, 5]
random.shuffle(numbers)
print("Shuffled list:", numbers)
