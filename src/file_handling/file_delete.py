# file_delete.py

import os

file_to_remove = "/storage/emulated/0/python_practice_project/file_to_delete.txt"

print(f"--- Attempting to delete '{file_to_remove}' ---")

if os.path.exists(file_to_remove):
    try:
        os.remove(file_to_remove)
        print(f"Successfully deleted '{file_to_remove}'.")
    except Exception as e:
        print(f"Error deleting file: {e}")
else:
    print(f"File '{file_to_remove}' does not exist, so cannot delete.")

print("\n[Program finished]")
