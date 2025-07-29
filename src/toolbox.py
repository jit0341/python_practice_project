# toolbox.py

import os
import zipfile

def rename_files(folder, prefix="file"):
    for i, filename in enumerate(os.listdir(folder)):
        new_name = f"{prefix}_{i+1}{os.path.splitext(filename)[1]}"
        os.rename(os.path.join(folder, filename), os.path.join(folder, new_name))

def zip_folder(folder_path, zip_name):
    with zipfile.ZipFile(zip_name, 'w') as zipf:
        for root, _, files in os.walk(folder_path):
            for file in files:
                full_path = os.path.join(root, file)
                zipf.write(full_path, os.path.relpath(full_path, folder_path))

def say_hello(name="Friend"):
    print(f"Hello, {name}! Welcome back.")
