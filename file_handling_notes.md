
Here are the commands we used to create and manage the four Python files related to file handling, organized for your record:
Commands for Python File Handling (for your record)
All these Python files were created and run in your /storage/emulated/0/python_practice_project/ directory.
1. Creating and Writing to my_notes.txt (via file_handling_write.py and file_handling_append.py)
To create/update my_notes.txt with initial content (using file_handling_write.py):
Python Code (inside file_handling_write.py):
# Ensure the file_path is correct for your project folder
file_path = "/storage/emulated/0/python_practice_project/my_notes.txt"
with open(file_path, "w") as file:
    file.write("This is my first file in Python!\n")
    file.write("Learning file handling is fun.")


To Run in Pydroid: Open file_handling_write.py and click the yellow play button.
To append content to my_notes.txt (using file_handling_append.py):
Python Code (inside file_handling_append.py):
# Ensure the file_path is correct for your project folder
file_path = "/storage/emulated/0/python_practice_project/my_notes.txt"
with open(file_path, "a") as file: # 'a' for append mode
    file.write("\nThis line was appended.")
    file.write("\nAnother line for append test.")


To Run in Pydroid: Open file_handling_append.py and click the yellow play button.
2. Reading from my_notes.txt (using three different methods)
a) Reading the entire file (file_read_entire.py):
Python Code (inside file_read_entire.py):
file_path = "/storage/emulated/0/python_practice_project/my_notes.txt"
with open(file_path, "r") as file:
    content = file.read()
    print(content)


To Run in Pydroid: Open file_read_entire.py and click the yellow play button.
b) Reading line by line (file_read_line_by_line.py):
Python Code (inside file_read_line_by_line.py):
file_path = "/storage/emulated/0/python_practice_project/my_notes.txt"
with open(file_path, "r") as file:
    for line in file:
        print(line.strip())


To Run in Pydroid: Open file_read_line_by_line.py and click the yellow play button.
c) Reading all lines into a list (file_read_all_lines_list.py):
Python Code (inside file_read_all_lines_list.py):
file_path = "/storage/emulated/0/python_practice_project/my_notes.txt"
with open(file_path, "r") as file:
    all_lines = file.readlines()
    print(all_lines)
    # Optional: iterate and print
    for line in all_lines:
        print(line.strip())


To Run in Pydroid: Open file_read_all_lines_list.py and click the yellow play button.
This list provides the core Python code snippets for each file, along with how to run them in Pydroid.
