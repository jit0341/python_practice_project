# Dunder Methods (Double Underscore Methods) in Python

# __init__ → Constructor
# __str__, __repr__ → String representations
# __len__ → Length of object
# __getitem__, __setitem__ → Indexing
# __iter__, __next__ → Iteration
# __eq__, __lt__, __le__, __gt__, __ge__, __ne__ → Comparison
# __add__, __sub__, __mul__, __truediv__ → Operator overloading
# __contains__ → in operator
# __call__ → Callable objects
# __enter__, __exit__ → Context manager (with statement)

class Demo:
    def __init__(self, name, items):
        self.name = name
        self.items = items

    def __str__(self):
        return f"Demo(name={self.name}, items={self.items})"

    def __repr__(self):
        return f"<Demo Object: {self.name}>"

    def __len__(self):
        return len(self.items)

    def __getitem__(self, index):
        return self.items[index]

    def __setitem__(self, index, value):
        self.items[index] = value

    def __iter__(self):
        self._index = 0
        return self

    def __next__(self):
        if self._index < len(self.items):
            val = self.items[self._index]
            self._index += 1
            return val
        raise StopIteration

    def __eq__(self, other):
        return self.items == other.items

    def __lt__(self, other):
        return len(self.items) < len(other.items)

    def __add__(self, other):
        return Demo(self.name + "+" + other.name, self.items + other.items)

    def __contains__(self, item):
        return item in self.items

    def __call__(self, greeting):
        return f"{greeting}, I am {self.name}!"

    def __enter__(self):
        print("Entering context (with statement)")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("Exiting context (with statement)")
        return False  # Do not suppress exceptions


# 🔸 Testing All Dunder Methods
if __name__ == "__main__":
    demo1 = Demo("Box1", [1, 2, 3])
    demo2 = Demo("Box2", [4, 5])

    print("1. __str__:", demo1)
    print("2. __repr__:", repr(demo1))
    print("3. __len__:", len(demo1))
    print("4. __getitem__:", demo1[0])
    demo1[0] = 99
    print("5. __setitem__ (after change):", demo1[0])

    print("6. __iter__ and __next__:")
    for item in demo1:
        print("   Iterated item:", item)

    print("7. __eq__ (==):", demo1 == demo2)
    print("8. __lt__ (<):", demo1 < demo2)
    print("9. __add__ (+):", demo1 + demo2)

    print("10. __contains__ (in):", 2 in demo1)

    print("11. __call__ (function-like):", demo1("Hello"))

    print("12. __enter__ and __exit__ (with statement):")
    with Demo("WithBlock", [10, 20]) as d:
        print("   Inside with block:", d)
