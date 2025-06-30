# create_file_to_rename.py

temp_old_name = "/storage/emulated/0/python_practice_project/old_name.txt"

print(f"--- Creating temporary file: '{temp_old_name}' ---")

try:
    with open(temp_old_name, "w") as file:
        file.write("This file will be renamed.\n")
    print("Temporary file 'old_name.txt' created successfully.")
except Exception as e:
    print(f"Error creating temporary file: {e}")

print("\n[Program finished]")
