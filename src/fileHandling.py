def open_and_close_file(filename):
    try:
        with open(filename, 'w') as file:
            print(f"File {filename} opened and closed successfully.")
    except Exception as e:
        print(f"Error: {e}")

# Test the function
open_and_close_file('example.txt')