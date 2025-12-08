Absolutely. Here's the complete Python Quirks & Tools Cheatbook (Parts 1, 2, 3 + OOP + Web Scraping) in clean, copy-pasteable format. You can paste this into any .txt, .md, or .pdf document.


---

🐍 Python Quirks & Tools Cheatbook

(Mobile-Friendly | All Parts | No Emojis)


---

🔹 Part 1: Smart Tools & Built-in Quirks

1. Swapping without temp variable



a, b = b, a

2. Multiple assignment



x, y, z = 1, 2, 3

3. Chained comparison



18 <= age < 60

4. List comprehension



squares = [x**2 for x in range(10)]

5. Ternary (conditional) operator



msg = "Even" if x % 2 == 0 else "Odd"

6. Unpacking in loops



for i, val in enumerate(mylist):
    ...

7. Else with loop



for item in items:
    if item == target:
        break
else:
    print("Not found")

8. _ underscore variable



_, x = (1, 2)  # Discard 1

9. Truthiness short-circuit



a = input() or "default"

10. All and any



if all([cond1, cond2]): ...
if any([x > 5 for x in lst]): ...

11. Join strings



", ".join(["one", "two", "three"])

12. Get index with default



val = mydict.get("key", "not found")


---

🔹 Part 2: More Practical Quirks

13. Reverse a list



rev = mylist[::-1]

14. Zip for parallel iteration



for name, age in zip(names, ages):
    ...

15. Set for uniqueness



unique = list(set(mylist))

16. Sort with custom key



sorted(data, key=lambda x: x["name"])

17. **Use *args and kwargs



def foo(*args, **kwargs): ...

18. Use lambda functions



double = lambda x: x * 2

19. List flattening (nested)



flat = [item for sublist in biglist for item in sublist]

20. String slicing tricks



txt[::-1]         # reverse
txt[:5]           # first 5
txt[-5:]          # last 5

21. Namedtuple (like mini class)



from collections import namedtuple
Point = namedtuple("Point", "x y")
p = Point(1, 2)


---

🔹 Part 3: Debugging & Clean Code Shortcuts

22. Use __name__ == "__main__"



if __name__ == "__main__":
    main()

23. f-strings for clean formatting



name = "Alice"
print(f"Hello {name}")

24. With for file/context handling



with open("file.txt") as f:
    lines = f.readlines()

25. Ternary with function calls



print("Valid") if is_valid(x) else exit()

26. Short dict creation



d = {k: v for k, v in pairs}

27. Counter from collections



from collections import Counter
count = Counter("mississippi")

28. Dictionary merging



d3 = {**d1, **d2}


---

🔹 OOP Tools (Mini Toolkit)

29. Class with constructor and method



class Dog:
    def __init__(self, name):
        self.name = name
    def bark(self):
        print(f"{self.name} barks!")

30. @classmethod and @staticmethod



class MyClass:
    @classmethod
    def hello(cls):
        ...
    @staticmethod
    def greet():
        ...

31. Use __str__ and __repr__



class Book:
    def __str__(self):
        return "Book Info"

32. Inheritance



class Animal: ...
class Dog(Animal): ...

33. Private variables (_var)



self._hidden = 123  # Convention only

34. Property decorator



@property
def age(self):
    return self._age


---

🔹 Web Scraping Tools (Basics)

35. Using requests and BeautifulSoup



import requests
from bs4 import BeautifulSoup

res = requests.get("https://example.com")
soup = BeautifulSoup(res.text, "html.parser")
title = soup.title.text

36. Find all tags



links = soup.find_all("a")

37. Find by class or id



soup.find("div", {"class": "main"})

38. Get attribute value



link = soup.find("a")["href"]

39. Use headers to mimic browser



headers = {"User-Agent": "Mozilla"}
res = requests.get(url, headers=headers)


---

🔹 Bonus Tools

40. Use timeit for performance



import timeit
print(timeit.timeit("x = 2+2"))

41. Use pprint for readable output



from pprint import pprint
pprint(my_large_dict)

42. Python tricks with pathlib



from pathlib import Path
files = Path(".").glob("*.py")


---

