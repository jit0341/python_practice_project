products = ["Apple", "Banana", "Cherry", "Date", "Elderberry", "Fig", "Grape", "Honeydew"]
# Indices:  0         1         2         3         4           5        6        7
# Neg Idx: -8        -7        -6        -5        -4          -3       -2       -1
print(f"Products from cherry to fig: {products[2:6]}")
print(f"The first two products: {products[:2]}")
print(f"Last three products: {products[-3:]}")
print(f"All products except first one: {products[1:]}")
print(f"All products except last one: {products[:-1]}")