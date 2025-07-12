# my_file_utils.py

def read_text_file(filepath):
    """
    Reads content from a text file.
    Handles FileNotFoundError and PermissionError.
    """
    try:
        with open(filepath, 'r') as file:
            content = file.read()
        print(f"✅ Success: Read from '{filepath}'")
        return content
    except FileNotFoundError:
        print(f"❌ Error: File not found at '{filepath}'. Please check the path and filename.")
        return None
    except PermissionError:
        print(f"❌ Error: Permission denied when trying to read '{filepath}'. Check file permissions.")
        return None
    except Exception as e:
        print(f"❌ An unexpected error occurred while reading '{filepath}': {e}")
        return None

def write_text_file(filepath, content):
    """
    Writes content to a text file.
    Handles PermissionError.
    """
    try:
        with open(filepath, 'w') as file:
            file.write(content)
        print(f"✅ Success: Wrote to '{filepath}'")
        return True
    except PermissionError:
        print(f"❌ Error: Permission denied when trying to write to '{filepath}'. Check folder/file permissions.")
        return False
    except Exception as e:
        print(f"❌ An unexpected error occurred while writing to '{filepath}': {e}")
        return False

# You can add more file-related functions here later if you want!
# For example:
# def append_to_file(filepath, content):
#     # ... code to append ...
