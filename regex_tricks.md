# Python Regex Tricks & Patterns

## Basics

### Match digits, letters, words
```python
\d   # digit
\w   # word character
\s   # space
```

### Quantifiers
```python
+     # 1 or more
*     # 0 or more
?     # 0 or 1
{n}   # Exactly n
{n,}  # n or more
```

### Groups and OR
```python
(r'a|b')     # matches 'a' or 'b'
(r'(abc)+')  # group repeated
```

---

## Regex Practice Problems with Solutions

### 1. Extract all email addresses
```python
import re
text = "My email is test@example.com and yours is hello@domain.org"
emails = re.findall(r'\b[\w.-]+@[\w.-]+\.\w+\b', text)
print(emails)  # ['test@example.com', 'hello@domain.org']
```

---

### 2. Replace all digits with #
```python
re.sub(r'\d', '#', 'Phone: 9876543210')  # Phone: ##########
```

---

### 3. Find dates in format DD/MM/YYYY
```python
text = "My dob is 12/05/1998, yours is 05/11/2000"
dates = re.findall(r'\b\d{2}/\d{2}/\d{4}\b', text)
print(dates)
```

---

### 4. Validate strong password
```python
pattern = r'^(?=.*[A-Z])(?=.*[a-z])(?=.*\d).{8,}$'
bool(re.match(pattern, 'Strong123'))  # True
```

---

### 5. Capture words with repeated letters
```python
re.findall(r'\b\w*(\w)\1\w*\b', "I saw a cool moon and sweet sheep")  
# Matches words with repeated characters
```
