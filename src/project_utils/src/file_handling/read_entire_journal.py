try: # We'll talk about try-except more, but for now, it helps if the file isn't found
    with open("journal_entry_July_3.txt", "r") as my_diary:
        all_notes = my_diary.read() # Read EVERYTHING from the diary
        print("Here are all your notes:\n")
        print(all_notes)
except FileNotFoundError:
    print("Oops! It looks like 'journal_entry_July_3.txt' doesn't exist yet. Did you run the writing script?")

print("\nFinished reading the whole file.")
