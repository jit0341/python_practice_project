nums = [10, 20, 30, 40, 50, 60, 70]

#1. First three items
#2. Last 2 items
# 3. All except the first and last
# 4. Reverse the list
# 5. Every second item

print(f" first three items: {nums[:3]}")
print(f"Last 2 items: {nums[-2:]}")
print(f"All except the first and last :  {nums[1:-1]}")
print(f"Reverse the list : {nums[::-1]}")
print(f"Every second item : {nums[::2]}")