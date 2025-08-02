

---

🔹 What are __dunder__ or Magic Methods?

They are built-in methods that Python calls automatically in certain situations, like when you use +, compare objects, convert to string, etc.


---

✅ Common __dunder__ Methods & Their Use:

📌 1. __init__(self, ...)

Purpose: Constructor method. Called when an object is created.


class Dog:
    def __init__(self, name):
        self.name = name

📌 2. __str__(self)

Purpose: String representation. Called when you print an object.


def __str__(self):
    return f"Dog name is {self.name}"

📌 3. __repr__(self)

Purpose: Official string representation (for developers/debugging).


def __repr__(self):
    return f"Dog('{self.name}')"

📌 4. __len__(self)

Purpose: Used by len(obj)


def __len__(self):
    return len(self.name)

📌 5. __add__(self, other)

Purpose: Controls behavior of + operator.


def __add__(self, other):
    return self.age + other.age

📌 6. __eq__(self, other)

Purpose: Behavior of ==


def __eq__(self, other):
    return self.name == other.name

📌 7. __lt__, __le__, __gt__, __ge__

Purpose: For <, <=, >, >=



---

🧠 Other Useful Dunder Methods

Method	Use

__getitem__	For indexing (obj[i])
__setitem__	For setting (obj[i] = x)
__delitem__	For deleting items
__contains__	For in checks
__call__	Makes object callable like a function
__enter__ / __exit__	Context managers (with statement)
__iter__ / __next__	For iteration using loops
__bool__	For boolean checks (if obj)
__main__	Special built-in variable used to check if a file is being run directly (not imported).



---

🔸 What is __main__?

if __name__ == "__main__":
    print("This script is running directly")

If you run a script, __name__ becomes "__main__".

If you import that script in another file, __name__ becomes the module's name.



---

🧪 Try This Minimal Code:

class Sample:
    def __init__(self, value):
        self.value = value
    
    def __str__(self):
        return f"Value: {self.value}"
    
    def __len__(self):
        return len(str(self.value))
    
    def __add__(self, other):
        return Sample(self.value + other.value)

obj1 = Sample(10)
obj2 = Sample(20)

print(obj1)              # Calls __str__
print(len(obj1))         # Calls __len__
obj3 = obj1 + obj2       # Calls __add__
print(obj3)


---
Dunder Method	Purpose

__init__	Constructor – runs when object is created
__str__ / __repr__	Friendly and dev-readable object string
__len__	Makes object usable with len()
__getitem__ / __setitem__	Allow indexing and assignment like a list
__iter__ / __next__	Makes object iterable (for loop)
__eq__, __lt__, __add__	Custom comparison and math
__contains__	Enables in keyword
__call__	Make object behave like a function
__enter__ / __exit__	with context manager support



