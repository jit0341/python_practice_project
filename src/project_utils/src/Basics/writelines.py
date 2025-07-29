lines = ["Apple\n", "Banana\n", "Cherry\n","Mango\n"]
with open("fruits.txt", "w") as f:
    f.writelines(lines)