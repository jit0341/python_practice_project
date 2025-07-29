# file_read_entire.py

# Define the full path to your notes file.
# It's good practice to store paths in variables for clarity and easy updates.
file_path = "/storage/emulated/0/python_practice_project/my_notes.txt"

print("--- Reading entire file (.read()) ---")

# Use a try-except block for basic error handling.
# This helps catch issues like the file not existing.
try:
    # Open the file in "r" (read) mode.
    # The 'with' statement ensures the file is automatically closed afterwards,
    # even if an error occurs.
    with open(file_path, "r") as file:
        # The .read() method reads the entire content of the file
        # and returns it as a single string.
        content = file.read()
        print(content)
except FileNotFoundError:
    # This block runs if the specified file does not exist.
    print(f"Error: The file '{file_path}' was not found.")
except Exception as e:
    # This is a general catch-all for any other unexpected errors.
    print(f"An unexpected error occurred: {e}")

print("\n[Program finished]")
