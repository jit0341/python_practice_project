import os 

print("\n--- Automatic File Discovery and Copy ---")

# Define the directory to scan.
# '.' means the current directory where the script is run from.
# IMPORTANT: Ensure your actual media files (IMG-20250715-WA0003.jpg, etc.)
# are in this 'source_directory' when you run the script.
source_directory = '.' 
destination_directory = '.' # You can change this to a subfolder like 'copied_files_output/'

# Optional: Create destination directory if it doesn't exist
# if destination_directory != '.':
#     os.makedirs(destination_directory, exist_ok=True) 

# Get a list of all entries (files and subdirectories) in the source directory
all_entries = os.listdir(source_directory)

print(f"Scanning directory: '{source_directory}'")
print(f"Found entries: {all_entries}")

# --- Function to copy a file in binary mode (re-using for clarity) ---
def copy_binary_file_auto(source_path, destination_path, original_name):
    # print(f"  Attempting to copy '{original_name}' to '{destination_path}'...")
    if not os.path.exists(source_path):
        print(f"  Error: Source file '{original_name}' not found. Skipping copy.")
        return False

    try:
        with open(source_path, 'rb') as infile:
            content_bytes = infile.read()

        with open(destination_path, 'wb') as outfile:
            outfile.write(content_bytes)

        print(f"  Successfully copied '{original_name}' (size: {len(content_bytes)} bytes) to '{os.path.basename(destination_path)}'.")
        return True
    except Exception as e:
        print(f"  An error occurred during copying '{original_name}': {e}")
        return False


# --- Process Images ---
print("\n--- Processing Images (.jpg, .png) ---")
for entry in all_entries:
    full_path = os.path.join(source_directory, entry) 

    if os.path.isfile(full_path) and (entry.lower().endswith(".jpg") or entry.lower().endswith(".png")):
        print(f"  Found image file: {entry}")

        output_filename = "auto_copied_" + entry 
        output_full_path = os.path.join(destination_directory, output_filename)

        copy_binary_file_auto(full_path, output_full_path, entry)

# --- Process Audio Files ---
print("\n--- Processing Audio Files (.mp3, .wav) ---")
for entry in all_entries:
    full_path = os.path.join(source_directory, entry)
    if os.path.isfile(full_path) and (entry.lower().endswith(".mp3") or entry.lower().endswith(".wav")):
        print(f"  Found audio file: {entry}")
        output_filename = "auto_copied_" + entry
        output_full_path = os.path.join(destination_directory, output_filename)
        copy_binary_file_auto(full_path, output_full_path, entry)

# --- Process Video Files ---
print("\n--- Processing Video Files (.mp4, .avi) ---")
for entry in all_entries:
    full_path = os.path.join(source_directory, entry)
    if os.path.isfile(full_path) and (entry.lower().endswith(".mp4") or entry.lower().endswith(".avi")):
        print(f"  Found video file: {entry}")
        output_filename = "auto_copied_" + entry
        output_full_path = os.path.join(destination_directory, output_filename)
        copy_binary_file_auto(full_path, output_full_path, entry)


# --- Cleanup (for files created by this section) ---
print("\n--- Cleanup of Auto-Copied Files ---")
files_to_clean_up = []
for entry in os.listdir(destination_directory):
    if entry.startswith("auto_copied_"):
        files_to_clean_up.append(os.path.join(destination_directory, entry))

if files_to_clean_up:
    print(f"Found {len(files_to_clean_up)} auto-copied files for cleanup.")
    for file_path in files_to_clean_up:
        try:
            os.remove(file_path)
            print(f"  Removed '{os.path.basename(file_path)}'.")
        except Exception as e:
            print(f"  Error removing '{os.path.basename(file_path)}': {e}")
else:
    print("No auto-copied files found for cleanup.")

print("-" * 20 + "\n")

