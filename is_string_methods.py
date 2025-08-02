import keyword

# --- Demonstration ---
print("--- .is...() String Methods Demonstration ---")

# isalnum(): Checks if all characters are alphanumeric (letters or numbers).
print(f"'Python3'.isalnum() -> {'Python3'.isalnum()}")
print(f"'Python 3'.isalnum() -> {'Python 3'.isalnum()}")

# isalpha(): Checks if all characters are alphabetic (letters).
print(f"'Python'.isalpha() -> {'Python'.isalpha()}")
print(f"'Python3'.isalpha() -> {'Python3'.isalpha()}")

# isascii(): Checks if all characters are ASCII.
print(f"'hello'.isascii() -> {'hello'.isascii()}")
print(f"'café'.isascii() -> {'café'.isascii()}")

# isdecimal(): Checks if all characters are decimal characters (0-9).
print(f"'12345'.isdecimal() -> {'12345'.isdecimal()}")
print(f"'-123'.isdecimal() -> {'-123'.isdecimal()}")

# isdigit(): Checks if all characters are digits.
print(f"'123'.isdigit() -> {'123'.isdigit()}")
print(f"'\u00B2'.isdigit() -> {'\u00B2'.isdigit()}") # Unicode for superscript two

# isidentifier(): Checks if the string is a valid Python identifier.
print(f"'my_variable'.isidentifier() -> {'my_variable'.isidentifier()}")
print(f"'1st_var'.isidentifier() -> {'1st_var'.isidentifier()}")
print(f"'for'.isidentifier() -> {'for'.isidentifier()}")
print(f"Note: 'for' is a keyword, but .isidentifier() doesn't check this. keyword.iskeyword('for') -> {keyword.iskeyword('for')}")

# islower(): Checks if all cased characters are lowercase.
print(f"'hello world'.islower() -> {'hello world'.islower()}")
print(f"'Hello World'.islower() -> {'Hello World'.islower()}")

# isnumeric(): Checks if all characters are numeric characters.
print(f"'123'.isnumeric() -> {'123'.isnumeric()}")
print(f"'\u00B2'.isnumeric() -> {'\u00B2'.isnumeric()}")

# isprintable(): Checks if all characters are printable.
print(f"'Hello World!'.isprintable() -> {'Hello World!'.isprintable()}")
print(f"'Hello\\nWorld'.isprintable() -> {'Hello\nWorld'.isprintable()}")

# isspace(): Checks if all characters are whitespace characters.
print(f"'   '.isspace() -> {'   '.isspace()}")
print(f"' a '.isspace() -> {' a '.isspace()}")

# istitle(): Checks if the string is titlecased.
print(f"'Hello World'.istitle() -> {'Hello World'.istitle()}")
print(f"'hello world'.istitle() -> {'hello world'.istitle()}")

# isupper(): Checks if all cased characters are uppercase.
print(f"'HELLO'.isupper() -> {'HELLO'.isupper()}")
print(f"'Hello'.isupper() -> {'Hello'.isupper()}")

