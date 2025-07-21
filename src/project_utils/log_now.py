fillename ="log_today.txt"
with open ("filename","w") as file:
	file.write("This is first line.\n")
	file.write("Learning file handling is fun.\n")
with open ("filename","r") as file:
	content = file.read()
	print ("Contents of the file:")
	print(content)
	
with open ("filename","a") as file:
	file.write("This is an added line.\n")
	file.write("We are now using append mode.\n")
with open ("filename","r") as file:
	content =	file.read()
	print ("Updated contents;")
	print(content)
	
with open ("filename","r") as file:
	print ("Current pointer position",file.tell())
	content =file.read(10)
	print ("After reading 10 character,  pointer is at:",file.tell())
	
with open("filename", "r") as file:
    file.seek(5)  # Move to 6th byte (starting from 0)
    content = file.read(10)
    print("Reading from 6th byte:", content)
print(f"Log file saved at: {filename}")