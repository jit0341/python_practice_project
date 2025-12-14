import os

# Default folder to save all text files
DEFAULT_FOLDER = os.path.join(os.path.dirname(__file__), "..", "text_notes")
os.makedirs(DEFAULT_FOLDER, exist_ok=True)

def save_to_txt(filename, content, mode="w"):
    """
    Save content to a .txt file in the default text_notes/ folder.
    """
    full_path = os.path.join(DEFAULT_FOLDER, filename)
    with open(full_path, mode) as f:
        f.write(content)
        print(f"[✓] Saved to {full_path}")

def save_data_as_log(filename, data_dict, mode="w"):
    """
    Save a dictionary of key-value pairs into a text file in clean format.
    """
    content = ""
    for key, value in data_dict.items():
        content += f"{key}: {value}\n"
    
    save_to_txt(filename, content, mode)