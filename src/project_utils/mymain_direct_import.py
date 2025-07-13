# mymain_direct_import.py

# Assuming 'generate_full_name', 'sum_two_nums', 'gravity', 'person' are in mymodule.py
from mymodule import generate_full_name, sum_two_nums, gravity, person

# Test generate_full_name
print(f"Full name: {generate_full_name('John', 'Doe')}")

# Test sum_two_nums
print(f"Sum of 1 and 9: {sum_two_nums(1, 9)}")

# Test gravity variable
mass = 100
weight = mass * gravity
print(f"Weight of 100kg object: {weight:.2f} Newtons") # .2f for 2 decimal places

# Test person dictionary
print(f"Person's first name: {person['firstname']}")

