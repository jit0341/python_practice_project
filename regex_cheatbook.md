Great! Here's a complete, copy-paste friendly Regex Cheatbook that you can use as a personal reference or paste into any file or notes app.


---

✅ Regex (Regular Expression) Cheatbook for Python

📌 What is Regex?

Regex (Regular Expression) is a sequence of characters that defines a search pattern, primarily used for string matching and manipulation.

In Python, import the re module:

import re


---

🔹 Common Regex Patterns

Pattern	Description

.	Any character except newline
\d	Digit (0–9)
\D	Non-digit
\w	Word character (letters, digits, _)
\W	Non-word character
\s	Whitespace (space, tab, newline)
\S	Non-whitespace
^	Start of string
$	End of string
[...]	Matches any one character inside brackets
[^...]	Negation: not any of the characters
`a	b`
()	Grouping
\b	Word boundary
\B	Not a word boundary



---

🔹 Quantifiers

Quantifier	Meaning

*	0 or more
+	1 or more
?	0 or 1
{n}	Exactly n times
{n,}	n or more times
{n,m}	Between n and m times



---

🔹 Regex Flags (Modifiers)

Flag	Effect

re.IGNORECASE or re.I	Case-insensitive matching
re.MULTILINE or re.M	^ and $ match start/end of each line
re.DOTALL or re.S	. matches newline too
re.VERBOSE or re.X	Allow comments and whitespace in pattern


Example:

re.search(r"hello", "Hello", re.IGNORECASE)


---

🔹 Useful Regex Tricks

✅ Extract All Emails

re.findall(r"[\w\.-]+@[\w\.-]+", text)

✅ Find All Words

re.findall(r"\b\w+\b", text)

✅ Extract Phone Numbers

re.findall(r"\d{10}", text)

✅ Replace All Digits With X

re.sub(r"\d", "X", text)

✅ Find Sentences Starting with a Word

re.findall(r"^Hello.*", text, re.MULTILINE)


---

🔹 Validate Patterns

Type	Regex

Email	[\w\.-]+@[\w\.-]+\.\w+
Phone	\d{10}
ZIP Code (India)	\d{6}
Username	^[a-zA-Z0-9_]{3,20}$
Strong Password	(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}



---

🔹 Real Examples

text = "Contact me at hello@example.com or call 9876543210."

# Extract email
emails = re.findall(r"[\w\.-]+@[\w\.-]+", text)

# Extract phone
phones = re.findall(r"\d{10}", text)

# Replace digits
masked = re.sub(r"\d", "*", text)

print(emails)  # ['hello@example.com']
print(phones)  # ['9876543210']
print(masked)  # 'Contact me at hello@example.com or call **********.'


---

🔹 Testing & Tools

Tool	Use

regex101.com	Test regex with explanation
pythex.org	Python-style regex tester
VS Code Extension: Regex Previewer	Live preview in code



---

🔹 Practice Challenges

1. Extract hashtags: #\w+


2. Extract domains from email: (?<=@)[\w.]+


3. Match time format: \d{1,2}:\d{2}(?:\s?[APap][Mm])?


4. Find repeated words: \b(\w+)\s+\1\b


5. Clean HTML tags: <.*?>




---




