# file_read_all_lines_list.py

# Define the full path to your notes file.
file_path = "/storage/emulated/0/python_practice_project/my_notes.txt"

print("--- Reading all lines into a list (.readlines()) ---")

try:
    # Open the file in "r" (read) mode.
    with open(file_path, "r") as file:
        # The .readlines() method reads all lines from the file
        # and returns them as a list of strings.
        # Each string in the list will include the newline character ('\n')
        # at the end of the line.
        all_lines = file.readlines()
        print(all_lines) # This will print the list directly

        # You can also iterate through the list if you want to print
        # each line on a new line without the list formatting:
        print("\n--- Printing lines from the list: ---")
        for line in all_lines:
            print(line.strip()) # Use .strip() to remove the newline character

except FileNotFoundError:
    print(f"Error: The file '{file_path}' was not found.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")

print("\n[Program finished]")
