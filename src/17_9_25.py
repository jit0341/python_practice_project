print("----- Square 1 to 30 --------")
i = 1
while i <= 30:
    print(f"Square of {i} is {i**2}")
    i += 1

print("-" * 40)

# Table with user input
n = int(input("Enter a number for its table: "))
print(f"------- Table of {n} -------")
for i in range(1, 11):
    print(f"{n} × {i} = {n * i}")

print("-" * 40)

# Fixed Table of 25
print("-------- Table of 25 --------")
i = 1
while i <= 10:
    print(f"25 × {i} = {25 * i}")
    i += 1

print("-" * 40)

# Fruits list
print("--- Iterate Name of Fruits ---")
fruits = ["Apple", "Banana", "Orange", "Grapes", "Peach"]
for fruit in fruits:
    print(f"I love {fruit}")

print("-" * 40)

# Teachers list
print("---- Teachers in RHS School ----")
teachers = [
    "Lakshman Sir", "Jitendra Bharti Sir", "Vinita Mam",
    "Nikki Soni Mam", "Jyoti Mam", "Pramila Mam",
    "Neeraj Sir", "Vikram Sir", "Pooja Mam"
]
for t in teachers:
    print(f"{t} teaches in RHS Digital School Lanchi, Surajpur")