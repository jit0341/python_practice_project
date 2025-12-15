# ==============================================
# PYTHON BASIC PROGRAMS – STUDY & REVISION FILE
# Teacher Style Explanation Included
# ==============================================



# ------------------------------------------
# Program 1: Check Even or Odd
# File: 01_check_even_odd.py
# ------------------------------------------

# 🔑 Key Concept:
# Modulus operator (%) and if-else

# 📥 Input:
# An integer number from the user

# 🧠 Logic:
# Check remainder when divided by 2

# 📤 Output:
# Print Even or Odd

# 👨‍🏫 Teacher Explanation:
# This program demonstrates the basic use of Python logic.
# It helps beginners understand how input, logic, and output
# are connected in a simple program.

# ===== Code Starts Here =====
"""
Program: Check if first number is even or odd
Input: List of numbers
Output: "Even" or "Odd"
Author: Jitendra Bharti
Date: 9 Dec 2024
"""
nums = [10,3,5,7,8]
if nums[0] % 2 ==0:
    print("Even")
else:
    print("Odd")

nums = [11,2,3,14]
if nums[0] % 2 ==0:
    print("Even")
elif nums[3] % 2 ==0:
    print("Even")
else:
    print("Odd")



# ===== Code Ends Here =====


# ------------------------------------------
# Program 2: Count Items in List
# File: 02_count_items.py
# ------------------------------------------

# 🔑 Key Concept:
# len() function

# 📥 Input:
# A predefined list

# 🧠 Logic:
# Count total elements using len()

# 📤 Output:
# Print total number of items

# 👨‍🏫 Teacher Explanation:
# This program demonstrates the basic use of Python logic.
# It helps beginners understand how input, logic, and output
# are connected in a simple program.

# ===== Code Starts Here =====
"""
Print total items count in a list
Author: Jitendra Bharti
"""
nums = [1,2,3,4,5]
print(len(nums))

nums = [2,3,80,40,'Python','Mobile']
print(len(nums))

# ===== Code Ends Here =====


# ------------------------------------------
# Program 3: Check Banana in List
# File: 03_check_banana.py
# ------------------------------------------

# 🔑 Key Concept:
# Membership operator (in)

# 📥 Input:
# A list of fruits

# 🧠 Logic:
# Check if 'banana' exists in list

# 📤 Output:
# Print found or not found

# 👨‍🏫 Teacher Explanation:
# This program demonstrates the basic use of Python logic.
# It helps beginners understand how input, logic, and output
# are connected in a simple program.

# ===== Code Starts Here =====
fruits = ["Apple","Banana","Mango"]
if "Banana" in fruits:
    print("Yes")
else:
    print("No")


# ===== Code Ends Here =====


# ------------------------------------------
# Program 4: First and Last Item
# File: 04_first_last_item.py
# ------------------------------------------

# 🔑 Key Concept:
# List indexing

# 📥 Input:
# A list

# 🧠 Logic:
# Access first and last index

# 📤 Output:
# Print first and last item

# 👨‍🏫 Teacher Explanation:
# This program demonstrates the basic use of Python logic.
# It helps beginners understand how input, logic, and output
# are connected in a simple program.

# ===== Code Starts Here =====
lst = [10,20,30,40]
print(lst[0], lst[-1])

"""
Program:Finding first number and the last number
Skills used: List slicing
Author: Jitendra Bharti
"""
illst = [12,20,30,40,50]
print(lst[0], lst[2], lst[-1])

nums = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
print(f"5th number from start: {nums[4]} and last 5th number: {nums[-5]}")
 
# fifth number from start digit and  5th number from last digit



# ===== Code Ends Here =====


# ------------------------------------------
# Program 5: Print Positive Numbers
# File: 05_print_positive_numbers.py
# ------------------------------------------

# 🔑 Key Concept:
# Loops and conditions

# 📥 Input:
# A list of numbers

# 🧠 Logic:
# Check numbers greater than zero

# 📤 Output:
# Print positive numbers

# 👨‍🏫 Teacher Explanation:
# This program demonstrates the basic use of Python logic.
# It helps beginners understand how input, logic, and output
# are connected in a simple program.

# ===== Code Starts Here =====
"""
Program: Print positive numbers
Skills: conditional for and if
Improvise: Bigger Numbers and count how mant positives
Author: Jitendra Bharti
"""
nums = [-2,3,-1,5,0]
for n in nums:
    if n>0:
        print(n)

num = [1,-1,2,-2,3,-3,0,-4,4,5,-5,6,-6,7,-7,8,-8,9,-9,10,-10,11,-11]
for n in num:
    if n>0:
        print(n)
l = len(n)
print(l)
        

    

# ===== Code Ends Here =====


# ------------------------------------------
# Program 6: Biggest of Three Numbers
# File: 06_biggest_of_three.py
# ------------------------------------------

# 🔑 Key Concept:
# Comparison and if-elif

# 📥 Input:
# Three numbers

# 🧠 Logic:
# Compare numbers

# 📤 Output:
# Print largest number

# 👨‍🏫 Teacher Explanation:
# This program demonstrates the basic use of Python logic.
# It helps beginners understand how input, logic, and output
# are connected in a simple program.

# ===== Code Starts Here =====
nums = []
for i in range(3):

    nums.append(int(input("Enter number:")))

print("Largest =", max(nums))

# ===== Code Ends Here =====


# ------------------------------------------
# Program 7: Sum Without sum()
# File: 07_sum_without_sum_function.py
# ------------------------------------------

# 🔑 Key Concept:
# Loop and accumulator

# 📥 Input:
# A list of numbers

# 🧠 Logic:
# Add numbers one by one

# 📤 Output:
# Print total sum

# 👨‍🏫 Teacher Explanation:
# This program demonstrates the basic use of Python logic.
# It helps beginners understand how input, logic, and output
# are connected in a simple program.

# ===== Code Starts Here =====
nums = [2,4,6,8]
total =0
for n in nums:
    total += n
    print(total)


# ===== Code Ends Here =====


# ------------------------------------------
# Program 8: Second Largest Number
# File: 08_second_largest.py
# ------------------------------------------

# 🔑 Key Concept:
# Sorting / logic

# 📥 Input:
# A list of numbers

# 🧠 Logic:
# Find second maximum

# 📤 Output:
# Print second largest

# 👨‍🏫 Teacher Explanation:
# This program demonstrates the basic use of Python logic.
# It helps beginners understand how input, logic, and output
# are connected in a simple program.

# ===== Code Starts Here =====
nums = [5,1,9,3,7]
num_sorted = sorted(nums)
print(num_sorted[-2])

# ===== Code Ends Here =====


# ------------------------------------------
# Program 9: Check Name in List
# File: 09_check_name.py
# ------------------------------------------

# 🔑 Key Concept:
# String comparison

# 📥 Input:
# Name and list

# 🧠 Logic:
# Compare input name with list

# 📤 Output:
# Print match result

# 👨‍🏫 Teacher Explanation:
# This program demonstrates the basic use of Python logic.
# It helps beginners understand how input, logic, and output
# are connected in a simple program.

# ===== Code Starts Here =====
names = ['Amit','Rahul','Priya']
if 'Rahul' in names:
    print("Found")


# ===== Code Ends Here =====


# ------------------------------------------
# Program 10: Temperature Check
# File: 10_temperature_above_40.py
# ------------------------------------------

# 🔑 Key Concept:
# Conditional check

# 📥 Input:
# Temperature value

# 🧠 Logic:
# Check if temperature > 40

# 📤 Output:
# Print warning message

# 👨‍🏫 Teacher Explanation:
# This program demonstrates the basic use of Python logic.
# It helps beginners understand how input, logic, and output
# are connected in a simple program.

# ===== Code Starts Here =====
temps = [32,41,29,45]
for t in temps:
    if t>40:
        print(f"High Temp:", t)


# ===== Code Ends Here =====
