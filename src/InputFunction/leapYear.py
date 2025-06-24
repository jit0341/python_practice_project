# Assignment- 3 

# Q1: Leap Year: Write a simple program to 
# determine if a given year is a leap year 
# using user input.

# leap year condition: 
# 4 divisible & 100 not divisible 
# 400 divisible

# user input 
year = int(input("Enter a Year (e.g. 2024): "))

# checking leap year
if (year % 4 == 0 and year % 100 != 0) or \
    (year % 400 == 0):
    print(f"{year} is leap year") 
else:
    print(f"{year} is not leap year") 
