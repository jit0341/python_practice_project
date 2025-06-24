# Q3: Admission Eligibility: A university has the following 
# eligibility criteria for admission:
# Marks in Mathematics >= 65
# Marks in Physics >= 55
# Marks in Chemistry >= 50
# Total marks in all three subjects >= 180 OR- 
# -Total marks in Mathematics and Physics >= 140
# Write a program that takes marks in three subjects as input and prints whether the student is eligible for admission.

# user input 
print("Enter PCM marks out of 100")
physics_marks = int(input("Enter Physics marks: "))
Chemistry_marks = int(input("Enter Chemistry marks: "))
Maths_marks = int(input("Enter Maths marks: "))

# Eligibility checks
if (Maths_marks >= 65 and 
    physics_marks >= 55 and 
    Chemistry_marks >= 50 and 
    (Maths_marks + physics_marks + Chemistry_marks) >= 180 ) or \
    (Maths_marks + physics_marks) >= 140:
    print("You're eligible!")
else: 
    print("You're not eligible!")