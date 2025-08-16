# Variables and Data Types
name = "Alice"
age = 25
height = 5.6
is_student = True

print(f"Name: {name}, Age: {age}, Height: {height}, Student: {is_student}")

# Conditional
if age > 18:
    print("You are an adult.")
else:
    print("You are a minor.")

# Loop
for i in range(1, 4):
    print("Loop count:", i)

# Function
def greet(person):
    return f"Hello, {person}!"

print(greet("Alice"))  # ✅ Fixed missing parenthesis

# Your input
name = input("Enter your name: ")
age = int(input("Enter your age: "))
favourite_number = int(input("Enter your favourite number: "))

print(f"Hi {name}, you are {age} years old. Your favourite number is {favourite_number}.")

# Even or odd check
if favourite_number % 2 == 0:
    print("That's a nice even number!")
else:
    print("Odd choice, but cool!")

