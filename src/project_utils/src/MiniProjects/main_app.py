# main_app.py

# Step 1: Import our module
import my_file_utils
import os # We'll use this for file system operations to cause errors

print("--- Starting File Handling Demo ---")

# --- Scenario 1: Successfully create and read a file ---
print("\n--- Test 1: Successful File Operations ---")
test_file_1 = "my_document.txt"
if my_file_utils.write_text_file(test_file_1, "Hello, this is a test document."):
    read_content = my_file_utils.read_text_file(test_file_1)
    if read_content:
        print(f"Content read: '{read_content}'")
    # Clean up (optional)
    if os.path.exists(test_file_1):
        os.remove(test_file_1)
        print(f"Cleaned up '{test_file_1}'.")

# --- Scenario 2: File Not Found Error ---
print("\n--- Test 2: Handling FileNotFoundError ---")
non_existent_file = "non_existent_file.txt"
print(f"Attempting to read '{non_existent_file}'...")
my_file_utils.read_text_file(non_existent_file) # This should trigger FileNotFoundError

# --- Scenario 3: Permission Denied Error (How to make it happen) ---
print("\n--- Test 3: Handling PermissionError ---")

# Let's create a file and intentionally make it read-only for this test.
# This part is crucial for generating the PermissionError.

# 1. Create a dummy file
read_only_file = "protected_doc.txt"
with open(read_only_file, 'w') as f:
    f.write("This file is about to become read-only.")
print(f"Created '{read_only_file}'.")

# 2. Change permissions to read-only
# In Termux: Run 'chmod 444 protected_doc.txt' in your terminal where the file is.
# In Pydroid: This is trickier. You might need a separate file manager app on Android
#            that allows changing file permissions. If not possible, you'll have to
#            skip this specific PermissionError test, or try to write to a system
#            protected path (which is less controlled).
#            Alternatively, if Pydroid is new enough and has 'All Files Access'
#            you might be able to create a file in a restricted system path (e.g., /data/local/tmp if writable).
#            But setting a file to read-only via 'chmod' in Termux is the most direct way.

# Wait for you to manually set permissions in Termux/Pydroid if applicable
input(f"PLEASE PAUSE: Now, go to your terminal (Termux) or use a file manager (Pydroid) and make '{read_only_file}' read-only. Then press Enter here to continue.")

print(f"Attempting to write to read-only file '{read_only_file}'...")
my_file_utils.write_text_file(read_only_file, "Trying to write to a protected file.") # This should trigger PermissionError

# Clean up (try to make it writable and remove, this might also fail if still read-only)
print(f"\nAttempting to clean up '{read_only_file}'...")
try:
    if os.path.exists(read_only_file):
        # In Termux, you can make it writable again:
        os.chmod(read_only_file, 0o644) # Read/write for owner
        os.remove(read_only_file)
        print(f"Cleaned up '{read_only_file}'.")
except Exception as e:
    print(f"Could not clean up '{read_only_file}'. You might need to remove it manually: {e}")

print("\n--- Demo Finished ---")
