## A script for basic username 
# and password handling or 
# validation.

correct_username = "admin"
correct_password = 1234
username = str(input(" Enter username:"))
password = int(input("Enter Password: "))
if username == correct_username and password == correc_password:
    print("Login successful ")
else:
    print("Access Denied ")
