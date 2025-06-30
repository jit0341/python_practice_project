# create_temp_file.py

# Define the full path for the temporary file
temp_file_path = "/storage/emulated/0/python_practice_project/file_to_delete.txt"

print(f"--- Creating temporary file: '{temp_file_path}' ---")

try:
    # Open in write mode ('w') to create the file and add some content
    with open(temp_file_path, "w") as file:
        file.write("This is a temporary file.\n")
        file.write("It will be deleted by the next script.\n")
    print("Temporary file created successfully.")
except Exception as e:
    print(f"Error creating temporary file: {e}")

print("\n[Program finished]")
