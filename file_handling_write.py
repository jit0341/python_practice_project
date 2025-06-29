# Step 1: Open a file in write mode
file = open("my_notes.txt", "w")

# Step 2: Write some text
file.write("This is my first file in Python!\n")
file.write("Learning file handling is fun.")

# Step 3: Close the file
file.close()

import os

print("Current working directory:")
print(os.getcwd())


with open("/storage/emulated/0/my_notes.txt", "r") as file:
    content = file.read()
    print("File content:\n")
    print(content)