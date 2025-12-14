total_words = 0 # Start a counter for all words in the file

try:
    with open("journal_entry_July_3.txt", "r") as file_object:
        print("--- Content of your journal ---")
        for line in file_object:
            cleaned_line = line.strip() # Remove leading/trailing whitespace and the newline character
            print(f"[{cleaned_line}]") # Print the cleaned line

            # Now, let's count words in THIS specific line
            words_in_line = cleaned_line.split() # Split the line into a list of words
            total_words += len(words_in_line) # Add the count of words in this line to our total

except FileNotFoundError:
    print("Oops! It looks like 'journal_entry_July_3.txt' doesn't exist yet.")
    print("Please make sure you've run the previous writing script to create it.")
except Exception as e: # Good practice to catch other unexpected errors
    print(f"An unexpected error occurred: {e}")

# This line is outside the try-except, so it runs whether the file was found or not
print(f"\nTotal words in the journal: {total_words}")
