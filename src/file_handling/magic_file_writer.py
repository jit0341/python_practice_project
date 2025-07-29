# 'with open(...)' is like opening your magic backpack
# 'as my_file:' means we'll call the notebook inside 'my_file'
with open("my_second_notes.txt", "w") as my_file:
    my_file.write("Hello from the magic backpack!\n")
    my_file.write("This is so much safer because Python closes it automatically.\n")
    my_file.write("No more forgetting to close!")

print("Notes written and saved automatically in 'my_second_notes.txt'!")
