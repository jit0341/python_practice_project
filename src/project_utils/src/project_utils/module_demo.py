# src/module_demo.py

# --- 1. Basic Import ---
# Imports the entire math_operations module.
# You access its contents using module_name.item
import math_operations

print("--- Basic Import (import math_operations) ---")
print(f"Sum: {math_operations.add(10, 5)}")
print(f"Product: {math_operations.multiply(8, 2)}")
print(f"Value of PI: {math_operations.PI}")
print("-" * 30)

# --- 2. Importing Specific Items ---
# Imports only specific functions/variables.
# You can use them directly without the module prefix.
from math_operations import subtract, PI

print("--- Importing Specific Items (from math_operations import subtract, PI) ---")
print(f"Difference: {subtract(20, 7)}")
print(f"Value of PI (again): {PI}") # Note: This PI is the same as math_operations.PI
print("-" * 30)

# --- 3. Aliasing Imports ---
# Imports with an 'as' keyword to give a shorter or different name.
import math_operations as mo
from math_operations import divide as div

print("--- Aliasing Imports (import ... as ...) ---")
print(f"Using alias 'mo': {mo.add(100, 20)}")
print(f"Using alias 'div': {div(50, 5)}")
print(f"Using alias 'div' with zero: {div(10, 0)}")
print("-" * 30)

# Example of using a standard library module
import random

print("--- Using a Standard Library Module (random) ---")
print(f"Random number between 1 and 100: {random.randint(1, 100)}")
print("-" * 30)
