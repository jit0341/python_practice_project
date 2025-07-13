# save as: permission_test.py

file_path = "/root/secret.txt"  # Restricted path

try:
    with open(file_path, 'r') as file:
        content = file.read()
        print(content)
except PermissionError:
    print("❌ Permission denied. You are not allowed to read this file.")
except FileNotFoundError:
    print("⚠️ File not found.")
except Exception as e:
    print(f"Unexpected error: {e}")