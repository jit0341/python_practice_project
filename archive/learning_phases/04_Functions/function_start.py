def multiply(a,b):
     return  a * b

print(multiply(5,3))

def greet_person(name, time="morning"):
    print(f"Good {time}, {name}!")

# Test it
greet_person("Jitendra")           # Output: Good morning, Jitendra!
greet_person("Keshav", "evening")  # Output: Good evening, Keshav!

def find_max(x, y, z):
    return max(x, y, z)

# Test it
print(find_max(15, 27, 9))  # Output: 27