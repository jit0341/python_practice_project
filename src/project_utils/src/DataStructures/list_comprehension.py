print("\n--- 8. List Comprehensions ---")
numbers = [1, 2, 3, 4, 5]

# Example 1: Create a list of squares
squares = [x**2 for x in numbers]
print(f"Squares: {squares}") # Output: Squares: [1, 4, 9, 16, 25]

cubes = [x**3 for x in numbers]
print(f"Cubes: {cubes}")


# Example 2: Create a list of even numbers (with a condition)
even_numbers = [x for x in numbers if x % 2 == 0]
print(f"Even numbers: {even_numbers}") # Output: Even numbers: [2, 4]

# Example 3: Transform strings to uppercase
fruits = ["apple", "banana", "cherry"]
uppercase_fruits = [fruit.upper() for fruit in fruits]
print(f"Uppercase fruits: {uppercase_fruits}") # Output: Uppercase fruits: ['APPLE', 'BANANA', 'CHERRY']