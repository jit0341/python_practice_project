✅ 2. Python: Core Essentials Cheat Sheet (Beginner to Intermediate)

Concept	Code Snippet / Tip
```
Write to file	open("file.txt", "w").write("text")
Read a file	open("file.txt", "r").read()
Loop over list	for item in my_list: print(item)
If condition	if x > 0: print("positive")
Function	def greet(name): return "Hi " + name
List methods	append(), remove(), sort(), reverse()
String methods	lower(), upper(), split(), join()
Dict access	my_dict["key"]
Import module	import math
Use f-string	name = "Jitendra"; print(f"Hello {name}")

```
# 🐍 Python Cheat Sheet — Core Concepts

## 📁 File Handling
```python
file = open("file.txt", "w")
file.write("Hello!")
file.close()

Loops

for i in range(5):
    print(i)

Conditionals

if x > 0:
    print("Positive")
elif x == 0:
    print("Zero")
else:
    print("Negative")

📦 Functions

def greet(name):
    return f"Hello {name}"

🧺 Lists & Methods

Method	Description

append()	Add item
remove()	Remove item
sort()	Sort list
reverse()	Reverse list


🔤 Strings

Method	Example

lower()	'ABC'.lower()
split()	'a b c'.split()
join()	' '.join(['a','b'])


📘 Extra Tips

Use import math, import os
Use f"{var}" for cleaner formatting
