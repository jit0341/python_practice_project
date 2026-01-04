fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for x in fruits:
  if "a" in x:
    newlist.append(x)

print(newlist)

fruits = ["Apple", "Banana", "Cherry", "Date", "Elderberry"]

for fruit in fruits:
    print(fruit) # This prints each fruit as the loop progresses
    if fruit == "Cherry":
        print("Cherry found! Stopping search.")
        break # This stops the loop immediately

print("Search complete.") # This line is executed after the loop finishes (or breaks)

