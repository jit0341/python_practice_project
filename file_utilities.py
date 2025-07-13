# file_utilities.py

def read_text_file(filename):
    """
    Reads content from a text file.
    Handles FileNotFoundError and PermissionError.
    """
    try:
        with open(filename, 'r') as f: # Try to open for reading ('r')
            content = f.read()
        print(f"✅ Success: Read from '{filename}'.")
        return content
    except FileNotFoundError:
        print(f"❌ Error: File '{filename}' not found. Please check the name and path.")
        return None
    except PermissionError:
        print(f"❌ Error: Permission denied when trying to read '{filename}'.")
        return None
    except Exception as e: # Catch any other unexpected errors
        print(f"❌ An unexpected error occurred while reading '{filename}': {e}")
        return None

def write_text_file(filename, content):
    """
    Writes content to a text file.
    Handles PermissionError.
    """
    try:
        with open(filename, 'w') as f: # Try to open for writing ('w')
            f.write(content)
        print(f"✅ Success: Wrote to '{filename}'.")
        return True
    except PermissionError:
        print(f"❌ Error: Permission denied when trying to write to '{filename}'. Check folder/file permissions.")
        return False
    except Exception as e: # Catch any other unexpected errors
        print(f"❌ An unexpected error occurred while writing to '{filename}': {e}")
        return False
