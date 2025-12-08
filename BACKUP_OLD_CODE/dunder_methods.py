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
        # __repr__: Provides an official string representation for developers.
        return f"Vector(x={self.x}, y={self.y})"

    def __add__(self, other):
        # __add__: Implements the addition operator (+).
        if isinstance(other, Vector):
            return Vector(self.x + other.x, self.y + other.y)
        return NotImplemented

    def __len__(self):
        # __len__: Implements the len() function.
        return 2

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

# --- Demonstration ---
print("--- Dunder Methods Demonstration ---")
v1 = Vector(1, 2)
v2 = Vector(3, 4)
v3 = Vector(1, 2)

print(f"\nString representation: {v1}")
print(f"Official representation: {repr(v1)}")
v4 = v1 + v2
print(f"Result of v1 + v2: {v4}")
print(f"Length of v1: {len(v1)}")
print(f"Is v1 equal to v2? {v1 == v2}")
print(f"Is v1 equal to v3? {v1 == v3}")
print(f"First component of v1: {v1[0]}")

