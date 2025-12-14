file_name = "journal_entry_July_3.txt"
total_words = 0

print("--- Step 1: Writing to the journal ---")
try:
    # Use 'w' mode to create/overwrite the file
    with open(file_name, "w") as my_diary:
        my_diary.write("Hello, today I updated my main README.md file.\n")
        my_diary.write("I learned about 'with open' command for file handling.\n")
        my_diary.write("It's great that Python closes the file automatically!")
    print(f"Notes successfully written to '{file_name}'.")

except Exception as e:
    print(f"Error writing to file: {e}")
    # If writing fails, we can't proceed to read
    exit() # This stops the script if there's a writing error

print("\n--- Step 2: Reading from the journal and counting words ---")
try:
    # Now, open the same file in 'r' mode to read
    with open(file_name, "r") as file_object:
        print("Content of your journal:")
        for line in file_object:
            cleaned_line = line.strip() # Remove leading/trailing whitespace and newline
            print(f"[{cleaned_line}]")

            words_in_line = cleaned_line.split()
            total_words += len(words_in_line)

except FileNotFoundError:
    # This theoretically should not happen if writing just succeeded,
    # but we keep it for robustness.
    print(f"Oops! The file '{file_name}' was not found after writing. This is unexpected.")
except Exception as e:
    print(f"An unexpected error occurred while reading: {e}")

print(f"\nTotal words in the journal: {total_words}")
