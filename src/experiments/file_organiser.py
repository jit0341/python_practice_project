import os
import shutil

# Step1. Ask the user for folder path
path  = input("Enter folder path:")

# Step2 Check if folder exists
if not os.path.exists(path):
    print("Error: The folder does not exist.")
else:
# Step3. List all files in the folder
    files = os.listdir(path)

    for file in files:
        file_path = os.path.join(path,file)

# Skip if it is a folder
        if os.pat.isdir(file_path):
            continue
# Separate file name and extension
        filename,extension = os.path.splitext(file)
        extension = extension[1:] # remove dot from ".txt" >>>>"txt"
        # Create folder for this extension.

        dest_folder = os.path.join(path,extesion)
        if not os.path.exists(dest_folder):



