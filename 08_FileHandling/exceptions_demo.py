# Basic try-except
try:
    num = int(input("Enter a number: "))
    result = 10 / num
    print("Result is:", result)
except ZeroDivisionError:
    print("Cannot divide by zero!")
except ValueError:
    print("Invalid input! Please enter a number.")

try:
    age = int(input("Enter your age: "))
except ValueError:
    print("That's not a valid number!")
else:
    print("You entered age:", age)
finally:
    print("This block always runs.")
    
    
   