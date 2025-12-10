# import the module
import os
# Creating a directory

# Changing the current directory
os.chdir("/storage/emulated/0/python_practice_project/src/project_utils")


# Getting current working directory
os.getcwd()
# Removing directory


# os_module_test.py

import os

# Define the directory name
test_dir_name = 'my_quick_dir'

# Creating a directory - Check if it exists first!
if not os.path.exists(test_dir_name):
    os.mkdir(test_dir_name)
    print(f"Directory '{test_dir_name}' created successfully.")
else:
    print(f"Directory '{test_dir_name}' already exists. Skipping creation.")

# Changing the current directory (ensure this path is correct for your system)
try:
    # Use a relative path if 'my_check_dir' is directly inside the current working directory
    # os.chdir(test_dir_name)

    # Or use the absolute path you mentioned, but ensure it's correct for your device
    # If this path is where your project lives, you might want to create my_check_dir there
    os.chdir('/storage/emulated/0/python_practice_project/src/project_utils')
    print(f"Changed current directory to: {os.getcwd()}")
except FileNotFoundError:
    print("Error: The specified directory for chdir was not found.")
except Exception as e:
    print(f"An error occurred changing directory: {e}")


# Getting current working directory
print(f"Current working directory after chdir: {os.getcwd()}")

# Removing directory (Only uncomment if you want to remove it and it's empty)
# First, you might need to change back to the parent directory if you chdir'd into it
# os.chdir('..')
# if os.path.exists(test_dir_name):
#     os.rmdir(test_dir_name)
#     print(f"Directory '{test_dir_name}' removed.")
# else:
#     print(f"Directory '{test_dir_name}' does not exist to remove.")

