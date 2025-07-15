# --- r+ Mode: Read and Write ---
print("--- r+ Mode ---")
try:
    with open("my_rplus_file.txt", "w") as f:
        f.write("Hello from r+ file!\n")
        f.write("This is the second line.\n")

    with open("my_rplus_file.txt", "r+") as f:
        content = f.read()
        print(f"Content before writing: \n{content}")

        # Move cursor to the beginning
        f.seek(0)
        f.write("NEW initial content. ")

        # Read again to see the changes
        f.seek(0)
        updated_content = f.read()
        print(f"Content after writing: \n{updated_content}")

except FileNotFoundError:
    print("Error: 'my_rplus_file.txt' not found for r+ mode.")
except Exception as e:
    print(f"An error occurred: {e}")

print("-" * 20 + "\n")

# --- w+ Mode: Write and Read ---
print("--- w+ Mode ---")
try:
    # First use w+ mode when file does not exist
    print("Scenario 1: File 'my_wplus_file_new.txt' does not exist initially.")
    with open("my_wplus_file_new.txt", "w+") as f:
        f.write("This is brand new content for w+ file.\n")
        f.seek(0) # Go back to the beginning to read what we just wrote
        content1 = f.read()
        print(f"Content after writing (new file): \n{content1}")

    print("\nScenario 2: File 'my_wplus_file_existing.txt' exists initially.")
    # Create an existing file first for demonstration
    with open("my_wplus_file_existing.txt", "w") as f:
        f.write("Original content for existing w+ file.\n")
        f.write("This line will be truncated.\n")

    # Now open the existing file in w+ mode
    with open("my_wplus_file_existing.txt", "w+") as f:
        f.write("New content overwrites old content.\n")
        f.seek(0) # Go back to the beginning
        content2 = f.read()
        print(f"Content after writing (existing file, truncated): \n{content2}")
        f.write("Appending more after reading.") # This will append to the current position (end)

    # Re-open in read mode to see final state of the existing file
    with open("my_wplus_file_existing.txt", "r") as f:
        final_content = f.read()
        print(f"Final content after re-opening (existing file): \n{final_content}")


except Exception as e:
    print(f"An error occurred in w+ mode: {e}")

print("-" * 20 + "\n")


# --- x Mode: Exclusive Creation ---
print("--- x Mode ---")

# Scenario 1: File does not exist (expected to succeed)
print("Scenario 1: Creating 'my_x_new_file.txt' (should succeed)")
try:
    with open("my_x_new_file.txt", "x") as f:
        f.write("This file was created exclusively with 'x' mode.\n")
    print("'my_x_new_file.txt' created successfully.")
except FileExistsError:
    print("'my_x_new_file.txt' already exists. (Unexpected in this scenario)")
except Exception as e:
    print(f"An unexpected error occurred: {e}")

# Scenario 2: File already exists (expected to fail with FileExistsError)
print("\nScenario 2: Trying to create 'my_x_new_file.txt' again (should raise FileExistsError)")
try:
    with open("my_x_new_file.txt", "x") as f:
        f.write("This should not be written.\n")
    print("'my_x_new_file.txt' created again. (This is an error, should not happen)")
except FileExistsError:
    print("Caught expected FileExistsError! 'my_x_new_file.txt' already exists.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")

# Clean up the file created for the first scenario, so it doesn't interfere with future runs
import os
try:
    if os.path.exists("my_x_new_file.txt"):
        os.remove("my_x_new_file.txt")
        print("\nCleaned up 'my_x_new_file.txt'.")
except Exception as e:
    print(f"Error cleaning up file: {e}")


print("-" * 20 + "\n")

# --- Binary Modes: rb, wb, ab ---
print("--- Binary Modes (rb, wb, ab) ---")

# --- 1. wb Mode (Write Binary) ---
print("\n--- wb Mode: Write Binary ---")
binary_data_to_write = b'\x48\x65\x6c\x6c\x6f\x20\x57\x6f\x72\x6c\x64\x21\x0a' # "Hello World!\n" in bytes
image_bytes = bytes([0xFF, 0xD8, 0xFF, 0xE0, 0x00, 0x10, 0x4A, 0x46, 0x49, 0x46, 0x00, 0x01]) # Small part of a JPEG header

try:
    with open("my_binary_file.bin", "wb") as f:
        f.write(binary_data_to_write)
        f.write(b'Some more bytes.\n')
        f.write(image_bytes)
    print("'my_binary_file.bin' created and written in binary mode.")
except Exception as e:
    print(f"Error in wb mode: {e}")

# --- 2. rb Mode (Read Binary) ---
print("\n--- rb Mode: Read Binary ---")
try:
    with open("my_binary_file.bin", "rb") as f:
        read_data = f.read()
        print(f"Content read from 'my_binary_file.bin': {read_data}")
        print(f"Type of read data: {type(read_data)}")

        # You can also read a specific number of bytes
        f.seek(0) # Go back to beginning
        first_10_bytes = f.read(10)
        print(f"First 10 bytes: {first_10_bytes}")
except FileNotFoundError:
    print("Error: 'my_binary_file.bin' not found for reading.")
except Exception as e:
    print(f"Error in rb mode: {e}")

# --- 3. ab Mode (Append Binary) ---
print("\n--- ab Mode: Append Binary ---")
more_binary_data = b'\x41\x70\x70\x65\x6e\x64\x65\x64\x20\x64\x61\x74\x61\x2e\n' # "Appended data.\n"

try:
    with open("my_binary_file.bin", "ab") as f:
        f.write(more_binary_data)
    print("'my_binary_file.bin' appended in binary mode.")

    # Verify by reading the whole file again
    with open("my_binary_file.bin", "rb") as f:
        final_read_data = f.read()
        print(f"Content after appending: {final_read_data}")
except Exception as e:
    print(f"Error in ab mode: {e}")

# --- Cleanup ---
import os
try:
    if os.path.exists("my_binary_file.bin"):
        os.remove("my_binary_file.bin")
        print("\nCleaned up 'my_binary_file.bin'.")
except Exception as e:
    print(f"Error cleaning up binary file: {e}")

print("-" * 20 + "\n")



