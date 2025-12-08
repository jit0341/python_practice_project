# test_toolbox.py
import os
import toolbox  # This will import your custom tools

# Test 1: Say Hello
toolbox.say_hello("Jitendra")

# Test 2: Rename files in a folder
# Make sure you have a folder named 'test_files' with some files inside it
toolbox.rename_files("test_files", prefix="renamed")

# Test 3: Zip a folder
# Make sure the folder exists before running thi

output_zip_path = os.path.join(os.getcwd(), "test_files_backup.zip")
toolbox.zip_folder("test_files", output_zip_path)
