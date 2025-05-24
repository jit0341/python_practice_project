score = 0

print("Welcome to the Python Quiz!")
print("-----------------------------")

# Question 1
answer = input("1. What is the output of 2 + 2? ")
if answer == "4":
    print("Correct!")
    score += 1
else:
    print("Wrong! The correct answer is 4.")

# Question 2
answer = input("2. What keyword is used to define a function in Python? ")
if answer.lower() == "def":
    print("Correct!")
    score += 1
else:
    print("Wrong! The correct answer is 'def'.")

# Question 3
answer = input("3. Which data type is used to store True or False? ")
if answer.lower() == "boolean" or answer.lower() == "bool":
    print("Correct!")
    score += 1
else:
    print("Wrong! The correct answer is 'bool'.")

# Question 4
answer = input("4. What is file extension name of files stored in Python?")
if answer. lower() == ".by":
   print("correct!")
   score += 1 
else:
    print("Wrong! The correct answer is '.py',")
print("-----------------------------")
print(f"You got {score} out of 4 questions correct.")
