# file_rename.py

import os

old_file_path = "/storage/emulated/0/python_practice_project/old_name.txt"
new_file_path = "/storage/emulated/0/python_practice_project/new_name.txt"

print(f"--- Attempting to rename '{old_file_path}' to '{new_file_path}' ---")

# Always check if the original file exists before trying to rename it.
if os.path.exists(old_file_path):
    try:
        os.rename(old_file_path, new_file_path)
        print(f"Successfully renamed '{old_file_path}' to '{new_file_path}'.")
    except FileExistsError:
        print(f"Error: A file named '{new_file_path}' already exists.")
    except Exception as e:
        print(f"Error renaming file: {e}")
else:
    print(f"Error: Original file '{old_file_path}' does not exist.")

print("\n[Program finished]")
