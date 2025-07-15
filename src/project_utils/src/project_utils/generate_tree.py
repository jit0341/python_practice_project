import os

# Define items to ignore
# You can add more here if needed, e.g., 'venv', '__pycache__', '.DS_Store'
IGNORE_ITEMS = ['.git', '__pycache__', 'venv', 'tree_output.txt', 'generate_tree.py'] 

def tree(path, indent=""):
    # Sort items for consistent output
    items = sorted(os.listdir(path))
    
    for item in items:
        # Skip ignored items
        if item in IGNORE_ITEMS:
            continue
        
        full_path = os.path.join(path, item)
        
        # Decide prefix for last item in a directory
        # This makes the tree look nicer with '└──' for the last item
        # (This part is a bit more advanced but makes the output cleaner)
        # However, for simplicity and Termux display, the original '├──' is often fine.
        # Let's stick to the original '├──' for now to avoid complexity in Termux display.
        
        print(indent + "├── " + item)
        
        if os.path.isdir(full_path):
            tree(full_path, indent + "│   ") # Increased indent to match common tree command output

# Run the tree generation from the current directory
tree(".")

