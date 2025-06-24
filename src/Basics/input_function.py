# Write a program to input student name & marks of 3 subjects. 
# Print name & percentage in output. 

student_name = input("Enter your name: ")
hindi_marks = input("Enter Hindi Marks: ")
maths_marks = input("Enter Maths Marks: ")
science_marks = input("Enter Science Marks: ") 

# calcualating percentage 
percentage = ((int(hindi_marks) + int(maths_marks) + int(science_marks))/300)*100

# # print result 
print(f"The result of {student_name} is {int(percentage)}%. Well done!!")
