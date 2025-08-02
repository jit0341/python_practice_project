import keyword

# --- Dunder Methods Demonstration ---

class Vector:
    """A simple class to demonstrate various dunder methods."""
    def __init__(self, x, y):
        self.x = x
        self.y = y
        # print(f"Vector initialized at ({self.x}, {self.y})") # Omitted for cleaner output

    def __str__(self):
        return f"Vector({self.x}, {self.y})"

    def __repr__(self):
        return f"Vector(x={self.x}, y={self.y})"

    def __add__(self, other):
        if isinstance(other, Vector):
            return Vector(self.x + other.x, self.y + other.y)
        return NotImplemented

    def __len__(self):
        return 2

    def __eq__(self, other):
        if isinstance(other, Vector):
            return self.x == other.x and self.y == other.y
        return NotImplemented

    def __getitem__(self, index):
        if index == 0:
            return self.x
        elif index == 1:
            return self.y
        else:
            raise IndexError("Vector index out of range")


# --- .is...() String Methods Demonstration ---

print("--- .is...() String Methods Demonstration ---")

# isalnum(): Checks if all characters are alphanumeric (letters or numbers).
print("\n--- .isalnum() ---")
print(f"'Python3' is alphanumeric: {'Python3'.isalnum()}")       # True
print(f"'Python 3' is alphanumeric: {'Python 3'.isalnum()}")     # False (due to space)
print(f"'Python_' is alphanumeric: {'Python_'.isalnum()}")      # False (due to underscore)

# isalpha(): Checks if all characters are alphabetic (letters).
print("\n--- .isalpha() ---")
print(f"'Python' is alphabetic: {'Python'.isalpha()}")           # True
print(f"'Python3' is alphabetic: {'Python3'.isalpha()}")         # False

# isascii(): Checks if all characters are ASCII.
print("\n--- .isascii() ---")
print(f"'hello' is ASCII: {'hello'.isascii()}")                   # True
print(f"'café' is ASCII: {'café'.isascii()}")                     # False

# isdecimal(): Checks if all characters are decimal characters (0-9).
print("\n--- .isdecimal() ---")
print(f"'12345' is decimal: {'12345'.isdecimal()}")               # True
print(f"'-123' is decimal: {'-123'.isdecimal()}")                 # False (due to hyphen)

# isdigit(): Checks if all characters are digits (including those for subscripts, etc.).
print("\n--- .isdigit() ---")
print(f"'123' is a digit string: {'123'.isdigit()}")               # True
print(f"'²' is a digit string: {'²'.isdigit()}")                   # True (Unicode superscript two)

# isidentifier(): Checks if the string is a valid Python identifier.
print("\n--- .isidentifier() ---")
print(f"'my_variable' is a valid identifier: {'my_variable'.isidentifier()}")   # True
print(f"'1st_var' is a valid identifier: {'1st_var'.isidentifier()}")           # False
print(f"'for' is a valid identifier: {'for'.isidentifier()}")                   # True (doesn't check keywords)
print(f"'for' is a keyword: {keyword.iskeyword('for')}")                        # Use this to check for keywords

# islower(): Checks if all cased characters in the string are lowercase.
print("\n--- .islower() ---")
print(f"'hello world' is lowercase: {'hello world'.islower()}")     # True
print(f"'Hello World' is lowercase: {'Hello World'.islower()}")     # False

# isnumeric(): Checks if all characters are numeric characters.
print("\n--- .isnumeric() ---")
print(f"'123' is numeric: {'123'.isnumeric()}")                     # True
print(f"'\u00B2' is numeric: {'\u00B2'.isnumeric()}")               # True (Unicode superscript two)

# isprintable(): Checks if all characters are printable or if the string is empty.
print("\n--- .isprintable() ---")
print(f"'Hello World!' is printable: {'Hello World!'.isprintable()}")  # True
print(f"'Hello\nWorld' is printable: {'Hello\nWorld'.isprintable()}")  # False (due to newline character)

# isspace(): Checks if all characters are whitespace characters.
print("\n--- .isspace() ---")
print(f"'   ' is space: {'   '.isspace()}")                           # True
print(f"' \t\n ' is space: {' \t\n '.isspace()}")                     # True
print(f"' a ' is space: {' a '.isspace()}")                           # False

# istitle(): Checks if the string is a titlecased string.
print("\n--- .istitle() ---")
print(f"'Hello World' is titlecased: {'Hello World'.istitle()}")       # True
print(f"'hello world' is titlecased: {'hello world'.istitle()}")       # False
print(f"'Hello world' is titlecased: {'Hello world'.istitle()}")       # False (the 'w' is not capitalized)

# isupper(): Checks if all cased characters in the string are uppercase.
print("\n--- .isupper() ---")
print(f"'HELLO' is uppercase: {'HELLO'.isupper()}")                   # True
print(f"'Hello' is uppercase: {'Hello'.isupper()}")                   # False
print("-" * 30)


# --- Dunder Methods Demonstration (cont.) ---
print("\n--- Dunder Methods Demonstration (cont.) ---")
# Create some Vector objects
v1 = Vector(1, 2)
v2 = Vector(3, 4)
v3 = Vector(1, 2)

# Using dunder methods
print(f"\nString representation (from __str__): {v1}")
print(f"Official representation (from __repr__): {repr(v1)}")
v4 = v1 + v2
print(f"Result of v1 + v2 (using __add__): {v4}")
print(f"Length of v1 (using __len__): {len(v1)}")
print(f"Is v1 equal to v2? (using __eq__): {v1 == v2}")
print(f"Is v1 equal to v3? (using __eq__): {v1 == v3}")
print(f"First component of v1 (using __getitem__): {v1[0]}")
print("-" * 30)

