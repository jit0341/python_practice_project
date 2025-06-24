# Q2: Login Authentication using conditional statement. 
# Assume you have a predefined username and password. 
# Write a program that prompts the user to enter a username and password and checks whether they match. 
# Provide appropriate messages for the following cases:
# Both username and password are correct.
# Username is correct but password is incorrect.
# Username is incorrect.

# predefined username and password
predefined_username = 'Madhav'
predefined_password = 'Pass101'

# prompts the user to enter a username and password 
username = input("Enter your username: ")
password = input("Enter your password: ")

# # username and password match 
if username == predefined_username:
    if password == predefined_password:
        print("Welcome! Login was successful.")
    else:
        print("Incorrect Password!")
else:
    print("Invalid Username!")
