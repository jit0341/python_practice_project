inventory = ["Laptop","Mouse","Keyboard","Monitor","Webcam","Speaker"]
print(inventory[0])
print(inventory[2])
print(inventory[-1])
inventory[1] = "Wireless Mouse"
inventory.append("Printer")
inventory.insert(1,"Headphones")
inventory.remove("Webcam")
item = inventory.pop()
print(item)
print(len(inventory))
print(f"First three items: {inventory[:3]}")
print(f"Third to last items: {inventory[2:]}")
print(f"Second to fourth items: {inventory[1:4]}")
print(f"Reverse order : {inventory[::-1]}")
print(f"Every second item: {inventory[::2]}")
print(f"Copy of item: {inventory[:]}")