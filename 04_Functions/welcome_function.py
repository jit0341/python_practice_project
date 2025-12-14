
def welcome(name):
    print(f"Hello, {name}! Keep coding!")

welcome("Jitendra")

def cube(n):
    return n ** 3

result = cube(9)
print("Cube is:", result)

def check_even_odd(n):
    if n % 2 == 0:
        return "Even"
    else:
        return "Odd"

print(check_even_odd(10))  # Output: Odd