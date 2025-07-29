# main_program.py

# Step 1: Import our module
import file_utilities
import os # We'll use this for cleaning up files

print("--- Starting File Handling Demo ---")

# --- Scenario 1: Successfully create and read a file ---
print("\n--- Test 1: Successful File Operations ---")
test_file_1 = "my_first_document.txt"
if file_utilities.write_text_file(test_file_1, "Hello from my first document!"):
    read_content = file_utilities.read_text_file(test_file_1)
    if read_content:
        print(f"Content read: '{read_content}'")
    # Clean up the file after testing
    if os.path.exists(test_file_1):
        os.remove(test_file_1)
        print(f"Cleaned up '{test_file_1}'.")

# --- Scenario 2: Triggering FileNotFoundError ---
print("\n--- Test 2: Handling FileNotFoundError ---")
non_existent_file = "this_file_does_not_exist.txt"
print(f"Attempting to read '{non_existent_file}'...")
file_utilities.read_text_file(non_existent_file) # This will trigger FileNotFoundError

# --- Scenario 3: Triggering PermissionError (Automatically) ---
print("\n--- Test 3: Handling PermissionError ---")
# We will try to write to a system-protected path.
# On unrooted Android (Termux/Pydroid), you typically don't have write access here.
# This will automatically cause a PermissionError without any manual steps.
protected_system_path = "/system/no_write_access.txt"
print(f"Attempting to write to protected path '{protected_system_path}'...")
file_utilities.write_text_file(protected_system_path, "Trying to write to a restricted area.") # This will trigger PermissionError

print("\n--- Demo Finished ---")
