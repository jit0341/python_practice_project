# safe_file_reader.py

def read_file_safely():
    filename = input("Enter the file name to read: ")

    try:
        with open(filename, 'r') as file:
            content = file.read()
            print("\n--- File Content ---")
            print(content)
            print("--------------------")

    except FileNotFoundError:
        print(f"❌ Error: '{filename}' not found.")
    except PermissionError:
        print(f"❌ Error: You don't have permission to read '{filename}'.")
    except Exception as e:
        print(f"❌ Unexpected error occurred: {e}")
    else:
        print("✅ File read successfully.")
    finally:
        print("📁 Program ended.")

# Run the function
read_file_safely()