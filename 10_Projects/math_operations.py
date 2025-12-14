# src/math_operations.py

PI = 3.14159

def add(a, b):
    """Adds two numbers."""
    return a + b

def subtract(a, b):
    """Subtracts two numbers."""
    return a - b

def multiply(a, b):
    """Multiplies two numbers."""
    return a * b

def divide(a, b):
    """Divides two numbers, handles division by zero."""
    if b == 0:
        return "Error: Cannot divide by zero!"
    return a / b

# This code will only run if math_operations.py is executed directly
# not when it's imported as a module
if __name__ == "__main__":
    print("This is math_operations.py being run directly!")
    print(f"PI value: {PI}")
    print(f"5 + 3 = {add(5, 3)}")
