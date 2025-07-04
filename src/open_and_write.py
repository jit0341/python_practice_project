notebook = open("my_first_notes.txt", "w")

# Now, let's write some messages into our notebook
notebook.write("Hello, world!\n") # The \n means "start a new line"
notebook.write("This is my first note in my Python notebook.\n")
notebook.write("It's fun to learn about files!")

print("I've written some things into the notebook!")

# IMPORTANT: We'll learn about this next, but for now, let's close it manually
notebook.close()
print("I've closed the notebook to save my notes.")
