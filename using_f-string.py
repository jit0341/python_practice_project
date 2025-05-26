## Demonstrates the usage of 
# f-strings for formatted string 
# literals in Python.

pi = 3.1415926535
print(f"Pi rounded to 3 decimal places: {pi:.3f}")
# Print only up to 3 decimal places
name = "Ravi"
math = 92
science = 88
print(f"{name} got {math} in Math and {science} in Science.")
# Output: "Ravi got 92 in Math and 88 in Science."
marks = 460
total = 500
percentage = (marks / total) * 100
print(f"Your percentage is: {percentage:.2f}%")
# Output: "Your percentage is: 92.00%"
a = 12
b = 8
print(f"The product of {a} and {b} is {a * b}.")
# Output: "The product of 12 and 8 is 96."
