# Let's create a temporary file with some messy lines for demonstration
with open("messy_lines.txt", "w") as f:
    f.write("  Hello, this is a test line with spaces. \n")
    f.write("Another line with a newline.\n")
    f.write("And a final line without a trailing newline.")

print("--- Reading messy_lines.txt WITHOUT .strip() ---")
with open("messy_lines.txt", "r") as f:
    for line in f:
        print(f"[{line}]") # Using [ ] to show where the line starts/ends

print("\n--- Reading messy_lines.txt WITH .strip() ---")
with open("messy_lines.txt", "r") as f:
    for line in f:
        print(f"[{line.strip()}]") # Now using .strip()
