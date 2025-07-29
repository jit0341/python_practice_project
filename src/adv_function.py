# 1 Default Arguments
def greet(name, message="Good Morning"):
    print(f"Hello {name}, {message}!")

greet("Jitendra")                 # Uses default
greet("Jitendra", "Welcome back!")  # Overrides defaul
greet(" Chatgpt", "Thank you! \n")


#✅ 2. *args — Variable Number of Positional Arguments

def total(*numbers):
    print("Numbers:", numbers)
    return sum(numbers)

print(total(10, 20, 30)) # Outputs: 60

print(total(100,34,450,22))

# 🧠 *args collects multiple arguments as a tuple.

print("--------")
# ✅ 3. **kwargs — Variable Number of Keyword Arguments

def profile(**details):
    for key, value in details.items():
        print(f"{key}: {value}")

profile(name="Jitendra", skill="Python", level="Intermediate")

# 🧠 **kwargs collects key-value pairs as a dictionary.

print("-------+++++---------")

# ✅ 4. Returning Multiple Values

def calc(a, b):
    return a+b, a-b, a*b , a/b

add, sub, mul , div = calc(12, 3)
print(f"Add: {add}, Sub: {sub}, Mul: {mul} ,Div: {div}")

print("------+++++++--------")

# ✅ 5. Docstrings (Function Documentation)

def square(n):
    """Returns the square of a number."""
    return n * n

print(square.__doc__)  # Access docstring

