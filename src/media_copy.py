import os

print("--- Working with Media Files (Binary Modes) ---")

# --- Setup: Define input and output file names ---
input_image_file = "IMG-20250715-WA0003.jpg"  # Make sure you have this file in your directory
output_image_file = "copied_IMG-20250715-WA0003.jpg"

input_audio_file = "Ae Kash Ke Hum - Kabhi Haan Kabhi Naa 128 Kbps.mp3"  # Optional: If you have an audio file
output_audio_file = "copied_Ae Kash Ke Hum - Kabhi Haan Kabhi Naa 128 Kbps.mp3"

input_video_file = "VID-20250710-WA0028.mp4"  # Optional: If you have a video file
output_video_file = "copied_VID-20250710-WA0028.mp4"

# --- Function to copy a file in binary mode ---
def copy_binary_file(source_path, destination_path):
    print(f"\nAttempting to copy '{source_path}' to '{destination_path}'...")
    if not os.path.exists(source_path):
        print(f"Error: Source file '{source_path}' not found. Skipping copy.")
        return False
    
    try:
        with open(source_path, 'rb') as infile:
            content_bytes = infile.read() # Read all bytes from the source

        with open(destination_path, 'wb') as outfile:
            outfile.write(content_bytes) # Write all bytes to the destination
        
        print(f"Successfully copied '{source_path}' (size: {len(content_bytes)} bytes).")
        return True
    except Exception as e:
        print(f"An error occurred during copying: {e}")
        return False

# --- Perform the copying for various media types ---
print("\n--- Image File Copy ---")
copy_binary_file(input_image_file, output_image_file)

print("\n--- Audio File Copy (Optional) ---")
copy_binary_file(input_audio_file, output_audio_file)

print("\n--- Video File Copy (Optional) ---")
copy_binary_file(input_video_file, output_video_file)

# --- Verification (Optional, but good practice) ---
print("\n--- Verification ---")
def verify_copy(original, copy):
    if not os.path.exists(original):
        return False, f"Original file '{original}' does not exist."
    if not os.path.exists(copy):
        return False, f"Copied file '{copy}' does not exist."
    
    original_size = os.path.getsize(original)
    copied_size = os.path.getsize(copy)

    if original_size != copied_size:
        return False, f"Sizes mismatch: Original ({original_size} bytes) vs Copy ({copied_size} bytes)."
    
    # For a more robust check, you could compare byte-by-byte or use hashing
    # For simplicity, we'll rely on size for now.
    
    return True, "Sizes match. Copy likely successful."

print(f"Verifying '{output_image_file}':")
success, msg = verify_copy(input_image_file, output_image_file)
print(f"  {success}: {msg}")

if os.path.exists(input_audio_file):
    print(f"Verifying '{output_audio_file}':")
    success, msg = verify_copy(input_audio_file, output_audio_file)
    print(f"  {success}: {msg}")

if os.path.exists(input_video_file):
    print(f"Verifying '{output_video_file}':")
    success, msg = verify_copy(input_video_file, output_video_file)
    print(f"  {success}: {msg}")


# --- Cleanup ---
print("\n--- Cleanup of Copied Files ---")
files_to_clean = [output_image_file, output_audio_file, output_video_file]
for f_name in files_to_clean:
    if os.path.exists(f_name):
        try:
            os.remove(f_name)
            print(f"Removed '{f_name}'.")
        except Exception as e:
            print(f"Error removing '{f_name}': {e}")

print("-" * 20 + "\n")

