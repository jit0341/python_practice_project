filename = input("Enter file name: ")

try:
    with open(filename, "r") as f:
        content = f.read()
        print("File content:\n", content)
except FileNotFoundError:
    print(f"❌ The file '{filename}' was not found.")
    
   