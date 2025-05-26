## Checks if a given number is 
# divisible by another number.

num = int(input("Enter a number: "))
if num % 3 == 0 and num % 5 == 0:
    print("Divisible by both 3 and 5")
elif num % 3 == 0:
    print("Only divisible by 3")
elif num % 5 == 0:
    print("Only divisible by 5")
else:
    print("Not divisible by 3 or 5")
