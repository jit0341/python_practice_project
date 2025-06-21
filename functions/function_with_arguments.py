def add_five(n):
    """
Args:
    n: A number to which 5 is added.
"""
    return n + 5
print(add_five(10)) # Output: 15

def is_even(n):
  """
  This function checks if a given number 'n' is even.

  Args:
    n: An integer.

  Returns:
    True if 'n' is even, False otherwise.
  """
  return n % 2 == 0

# Expected usage and output:
print(is_even(4)) # Output: True
print(is_even(7)) # Output: False


import math

def area_of_circle(radius):
  """
  Calculates the area of a circle given its radius.

  Args:
    radius: The radius of the circle (a number).

  Returns:
    The area of the circle.
  """
  return  math. pi * (radius ** 2)

# Expected usage and output:
print(area_of_circle(7)) # Output: 153.86


def say_hi(name):
  """
  Prints a greeting message including the given name.

  Args:
    name: A string representing the name.
  """
  print(f"Hi, {name}! Good to see you.")

# Q3 Expected usage:
say_hi("Alice")
# Output: Hi, Alice! Good to see you.

say_hi("Bob")
# Output: Hi, Bob! Good to see you.


def power(base, exponent):
  """
  Calculates the power of a base raised to an exponent.

  Args:
    base: The base number.
    exponent: The exponent.

  Returns:
    The base raised to the power of the exponent.
  """
  return base ** exponent

# Q4 Expected usage and output:
print(power(2, 3)) # Output: 8
print(power(5, 2)) # Output: 25
print(power(10, 0)) # Output: 1


