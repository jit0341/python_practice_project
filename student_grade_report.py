name = input("Enter student name: ")
math = int(input("Enter Math marks: "))
english = int(input("Enter English marks: "))
science = int(input("Enter Science marks: "))

total = math + english + science
percentage = (total / 300) * 100

print(f"\nStudent: {name}")
print(f"Math: {math}, English: {english}, Science: {science}")
print(f"Total: {total}/300")
print(f"Percentage: {percentage:.2f}%")
