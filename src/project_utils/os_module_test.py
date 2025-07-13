import os
# Create a new directory for testing
test_dir = 'my_test_dir'
if not os.path.exists(test_dir): # Check if it already exists to avoid error
    os.mkdir(test_dir)
    print(f"Directory '{test_dir}' created.")
else:
    print(f"Directory '{test_dir}' already exists.")

# Change to the new directory
os.chdir(test_dir)
print(f"Current working directory: {os.getcwd()}")

# Go back to the parent directory
os.chdir('..')
print(f"Current working directory after moving up: {os.getcwd()}")

# Clean up: remove the test directory (it must be empty)
# Uncomment the line below ONLY if you are sure the directory is empty
# os.rmdir(test_dir)
# print(f"Directory '{test_dir}' removed.")

# import the module
import os
# Creating a directory
my_third_dir = "a"
# Changing the current directory
os.chdir("/storage/emulated/0/python_practice_project/src/project_utils")
# Getting current working directory
os.getcwd()
# Removing directory


