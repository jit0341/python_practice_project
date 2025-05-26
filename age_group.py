## Python script to categorize
# a person's age into different age
# groups (e.g., child, teenager,
# adult).age = int(input("Enter your age: "))
if age < 0 or age > 120:
    print("Invalid age")
elif age <= 12:
    print("Child")
elif age <= 19:
    print("Teenager")
elif age <= 59:
    print("Adult")
else:
    print("Senior")
