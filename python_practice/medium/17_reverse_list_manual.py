# 1.Reverse without reverse()
nums = [10,20,30,40,50,60]
print(f"Original list: {nums}")
rev = []
for n in nums:
    rev.insert(0,n)
print(f"Reversed list: {rev}")

# 2. Using the list.reverse() Method
print("---Second Method----")
nums = [10,20,30,40,50,60]
print(f"Original list: {nums}")

# Reverse the list IN-PLACE
nums.reverse()
print(f"Reversed list: {nums}")

# 3. Using Slicing [::-1] (Non-In-Place)
print("\n----Third Method----")
original_nums = [10,20,30,40,50,60]
print(f"Original list: {original_nums}")

# Use slicing to create new reversed list
reversed_nums = original_nums[::-1]
print(f"Reversed list: {reversed_nums}")

# 4. Using the reversed() Function (Non-In-Place, returns an Iterator)
print("\n----Fourth Method--------")
original_nums = [10,20,30,40,50,60]
print(f"Original list: {original_nums}")
reversed_nums = list(reversed(original_nums))
print(f"Reversed list: {reversed_nums}")




