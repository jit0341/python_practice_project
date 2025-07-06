
# 📘 Python List Slicing Cheat Sheet

## 🔹 Sample List
```python
my_list = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
# Index:      0    1    2    3    4    5    6
# Negative:  -7   -6   -5   -4   -3   -2   -1
```

---

## 🔹 Syntax
```python
my_list[start : stop : step]
```

- `start`: index to begin from (inclusive)
- `stop`: index to stop before (exclusive)
- `step`: how many items to skip (optional)

---

## 🔹 Common Patterns

| Task                        | Code Example         | Output                          |
|----------------------------|----------------------|---------------------------------|
| First 3 items              | `my_list[:3]`         | `['A', 'B', 'C']`               |
| Last 2 items               | `my_list[-2:]`        | `['F', 'G']`                    |
| All except first & last    | `my_list[1:-1]`       | `['B', 'C', 'D', 'E', 'F']`     |
| Reverse the list           | `my_list[::-1]`       | `['G', 'F', 'E', 'D', 'C', ...]`|
| Every 2nd item             | `my_list[::2]`        | `['A', 'C', 'E', 'G']`          |
| Items from index 2 to 4    | `my_list[2:5]`        | `['C', 'D', 'E']`               |
| Copy entire list           | `my_list[:]`          | `['A', 'B', 'C', 'D', ...]`     |

---

## 🔹 Tips
- `start` is included ✅
- `stop` is excluded ❌
- Negative indices count from end ➡️

---

## 📎 Add Visual
To include an image cheat sheet in Markdown:

```markdown
![List Slicing Cheat Sheet](path_to_image.png)
```

![List Slicing Cheat Sheet](your_image_python_list_slicing_cheat_sheet.png>
