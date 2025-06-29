# file_handling_write.py

# Step 1: Open a file in write mode using the FULL path to your project folder
# This ensures my_notes.txt is created/updated inside your python_practice_project folder
file = open("/storage/emulated/0/python_practice_project/my_notes.txt", "w")

# Step 2: Write some text
file.write("This is my first file in Python!\n")
file.write("Learning file handling is fun.")

# Step 3: Close the file
file.close()

# The 'os' module allows interaction with the operating system
import os
# This prints Pydroid's default current working directory, useful for debugging
print("Current working directory (Pydroid's default):", os.getcwd())

# To read the file you just wrote, use the FULL path to your project folder
print("\nReading file content from the project folder:")
with open("/storage/emulated/0/python_practice_project/my_notes.txt", "r") as file:
    content = file.read()
    print(content)
