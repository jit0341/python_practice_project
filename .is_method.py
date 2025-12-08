# List of test strings to try
test_strings = [
    "123",          # digits only
    "Ⅻ",            # Roman numeral 12 (unicode)
    "٢",            # Arabic digit 2
    "hello",        # lowercase letters
    "HELLO",        # uppercase letters
    "Hello World",  # title case with space
    "abc123",       # alphanumeric
    "   ",          # spaces
    "!",            # punctuation
    "\n",           # newline (non-printable)
    "my_var1",      # valid identifier
]

# Functions to test
checks = [
    ("isdigit", str.isdigit),
    ("isnumeric", str.isnumeric),
    ("isdecimal", str.isdecimal),
    ("isalpha", str.isalpha),
    ("isalnum", str.isalnum),
    ("islower", str.islower),
    ("isupper", str.isupper),
    ("isspace", str.isspace),
    ("istitle", str.istitle),
    ("isidentifier", str.isidentifier),
    ("isprintable", str.isprintable),
]

# Run the checks
for s in test_strings:
    print(f"\nTesting: {repr(s)}")
    for name, func in checks:
        try:
            result = func(s)
            print(f"  {name:15} → {result}")
        except Exception as e:
            print(f"  {name:15} → ERROR: {e}") 

if __name__ == "__main__":
    test_strings = ["123", "abc", "abc123", "Hello World", "   ", "Ⅻ", "3.14", "_validName"]

    for s in test_strings:
        print(f"\nTesting: {repr(s)}")
        print(f"isdecimal:     {s.isdecimal()}")
        print(f"isdigit:       {s.isdigit()}")
        print(f"isnumeric:     {s.isnumeric()}")
        print(f"isalpha:       {s.isalpha()}")
        print(f"isalnum:       {s.isalnum()}")
        print(f"islower:       {s.islower()}")
        print(f"isupper:       {s.isupper()}")
        print(f"isspace:       {s.isspace()}")
        print(f"istitle:       {s.istitle()}")
        print(f"isidentifier:  {s.isidentifier()}")
        print(f"isprintable:   {s.isprintable()}")
