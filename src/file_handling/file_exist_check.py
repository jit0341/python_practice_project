# file_exists_check.py

# The 'os' module provides functions for interacting with the operating system,
# including file system operations.
import os

# Define the full path to your existing notes file
existing_file_path = "/storage/emulated/0/python_practice_project/my_notes.txt"

# Define a path to a file that *does not* exist (for demonstration)
non_existent_file_path = "/storage/emulated/0/python_practice_project/non_existent_file.txt"

# Define a path to your project directory (which is a folder)
project_folder_path = "/storage/emulated/0/python_practice_project/"


print("--- Checking for file existence ---")

# Check if a file exists using os.path.exists()
if os.path.exists(existing_file_path):
    print(f"'{existing_file_path}' exists.")
else:
    print(f"'{existing_file_path}' does NOT exist.")

# Check for a non-existent file
if os.path.exists(non_existent_file_path):
    print(f"'{non_existent_file_path}' exists.")
else:
    print(f"'{non_existent_file_path}' does NOT exist.")

print("\n--- Distinguishing between files and directories ---")

# Check if the path points to a file using os.path.isfile()
if os.path.isfile(existing_file_path):
    print(f"'{existing_file_path}' is a file.")
else:
    print(f"'{existing_file_path}' is NOT a file.")

# Check if the path points to a directory using os.path.isdir()
if os.path.isdir(project_folder_path):
    print(f"'{project_folder_path}' is a directory.")
else:
    print(f"'{project_folder_path}' is NOT a directory.")

print("\n[Program finished]")
