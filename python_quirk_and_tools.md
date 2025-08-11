# Python Quirks & Smart Tools

## Part 1 – Lesser-known but useful Python behaviors

### 1. Chained Comparison
```python
5 < x < 10  # True if x is between 5 and 10
```

### 2. Tuple Assignment
```python
a, b = b, a  # Swap values
```

### 3. Underscore Usage
```python
_ = some_unused_value  # To ignore values
```

### 4. For/Else, While/Else
```python
for item in my_list:
    if item == target:
        break
else:
    print("Target not found")
```

### 5. Mutable Default Arguments Quirk
```python
def append_to_list(x, mylist=[]):  # Don't do this!
    mylist.append(x)
    return mylist
```

### 6. `any()` vs `all()`
```python
any([False, True, False])  # True
all([True, True, True])    # True
```

---

## Part 2 – Useful One-Liners & Shortcuts

### 7. Flatten a list of lists
```python
flat = [item for sublist in nested_list for item in sublist]
```

### 8. Transpose a matrix
```python
zip(*matrix)
```

### 9. Get frequency count
```python
from collections import Counter
Counter('banana')
```

### 10. Merging two dictionaries
```python
{**dict1, **dict2}
```

### 11. Conditional assignment
```python
x = a if cond else b
```

---

## Part 3 – OOP, Web Scraping, Scripting

### 12. Simple Class with `__repr__`
```python
class Person:
    def __init__(self, name): self.name = name
    def __repr__(self): return f"Person('{self.name}')"
```

### 13. Web Scraping with BeautifulSoup
```python
from bs4 import BeautifulSoup
import requests
r = requests.get('https://example.com')
soup = BeautifulSoup(r.text, 'html.parser')
print(soup.title.text)
```

### 14. File Line Reverser Script
```python
with open('file.txt') as f:
    lines = f.readlines()[::-1]
```

### 15. Get all `.py` files from folder
```python
import os
files = [f for f in os.listdir('.') if f.endswith('.py')]
```

### 16. Simple Timer
```python
from time import time
start = time()
# code
print(f"Time: {time() - start:.2f}s")
```
