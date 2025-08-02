import keyword

# --- .isidentifier() Example ---
print("--- .isidentifier() Demonstration ---")
# Valid identifiers
print(f"'my_variable' is a valid identifier: {'my_variable'.isidentifier()}")
print(f"'_private_var' is a valid identifier: {'_private_var'.isidentifier()}")
print(f"'myFunc123' is a valid identifier: {'myFunc123'.isidentifier()}")

# Invalid identifiers
print(f"'1st_var' is a valid identifier: {'1st_var'.isidentifier()}")
print(f"'my-var' is a valid identifier: {'my-var'.isidentifier()}")
print(f"'for' is a valid identifier: {'for'.isidentifier()}") # .isidentifier() doesn't check keywords
print(f"'for' is a Python keyword: {keyword.iskeyword('for')}") # Use the keyword module for this check
print("-" * 30)


# --- Dunder Methods Demonstration ---

class Vector:
    """A simple class to demonstrate various dunder methods."""
    def __init__(self, x, y):
        # __init__: The constructor. Initializes object attributes.
        self.x = x
        self.y = y
        print(f"Vector initialized at ({self.x}, {self.y})")

    def __str__(self):
        # __str__: Provides a user-friendly string representation.
        return f"Vector({self.x}, {self.y})"

    def __repr__(self):
        # __repr__: Provides an official string representation.
        return f"Vector(x={self.x}, y={self.y})"

    def __add__(self, other):
        # __add__: Implements the addition operator (+).
        if isinstance(other, Vector):
            return Vector(self.x + other.x, self.y + other.y)
        return NotImplemented

    def __len__(self):
        # __len__: Implements the len() function.
        return 2  # A vector has a length of 2 (x and y components)

    def __eq__(self, other):
        # __eq__: Implements the equality operator (==).
        if isinstance(other, Vector):
            return self.x == other.x and self.y == other.y
        return NotImplemented

    def __getitem__(self, index):
        # __getitem__: Implements item access using brackets [].
        if index == 0:
            return self.x
        elif index == 1:
            return self.y
        else:
            raise IndexError("Vector index out of range")


print("--- Dunder Methods Demonstration ---")
# Create some Vector objects
v1 = Vector(1, 2)
v2 = Vector(3, 4)
v3 = Vector(1, 2)

# Using __str__ and __repr__
print(f"\nString representation (from __str__): {v1}")
print(f"Official representation (from __repr__): {repr(v1)}")

# Using __add__
v4 = v1 + v2
print(f"\nResult of v1 + v2 (using __add__): {v4}")

# Using __len__
print(f"\nLength of v1 (using __len__): {len(v1)}")

# Using __eq__
print(f"\nIs v1 equal to v2? (using __eq__): {v1 == v2}")
print(f"Is v1 equal to v3? (using __eq__): {v1 == v3}")

# Using __getitem__
print(f"\nFirst component of v1 (using __getitem__): {v1[0]}")
print(f"Second component of v1 (using __getitem__): {v1[1]}")

print("-" * 30)


