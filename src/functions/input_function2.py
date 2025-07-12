# Q2: Write a program that collects multiple types of data to store in a dictionary 
# and print output.

#  initializing a dictionary
user_data = {} 

# input from user
user_data['name'] = input("Enter your name: ")
user_data['age'] = int(input("Enter your age: "))
user_data['height'] = float(input("Enter your height: "))
user_data['student'] = input("Are you a student (yes/no)")

# print the input from user
print(user_data)