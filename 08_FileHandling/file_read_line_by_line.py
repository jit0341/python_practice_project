# file_read_line_by_line.py

# Define the full path to your notes file.
file_path = "/storage/emulated/0/python_practice_project/my_notes.txt"

print("--- Reading file line by line ---")

try:
    # Open the file in "r" (read) mode.
    with open(file_path, "r") as file:
        # When you iterate directly over a file object (like 'for line in file:'),
        # Python reads one line at a time.
        for line in file:
            # Each 'line' read will include the newline character ('\n') at the end.
            # .strip() is used to remove leading/trailing whitespace, including '\n'.
            print(line.strip())
except FileNotFoundError:
    print(f"Error: The file '{file_path}' was not found.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")

print("\n[Program finished]")
