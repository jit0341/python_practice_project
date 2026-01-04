# 1. Keyword Arguments

def introduce(name, age):
    print(f"My name is {name} and I am {age} years old.")

introduce(age=25, name="Jitendra")

# ➡️ Practice swapping argument order using keywords.

# 🔹 2. Variable-Length Arguments (*args, **kwargs)

# *args example
def add_all(*numbers):
    return sum(numbers)

print(add_all(1, 2, 3, 4, 5))  # Output: 15

# **kwargs example
def print_info(**data):
    for key, value in data.items():
        print(f"{key}: {value}")
print_info(name="Jitendra", subject="Python", level="Intermediate")

# ➡️ Practice: Write your own greet_all(*names) and describe_person(**details).


# 🧠 Mini Task

# Write a Python function:

def student_profile(name, age, *subjects, **marks):
    # Print name and age
    # Print list of subjects
    # Print subject-wise marks

