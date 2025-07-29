# file_handling_append.py

# Part 1: Appending to the file
print("--- Appending to file ---")
# Open the file in append mode ("a")
# Using the full path to ensure it's in your project folder
with open("/storage/emulated/0/python_practice_project/my_notes.txt", "a") as file:
    file.write("\nThis is a new line appended to the file.")
    file.write("\nAnother line added!")
print("Content appended successfully!")

# Part 2: Reading the entire file content after appending
print("\n--- Reading updated file content ---")
with open("/storage/emulated/0/python_practice_project/my_notes.txt", "r") as file:
    content = file.read()
    print(content)

print("\n[Program finished]")
