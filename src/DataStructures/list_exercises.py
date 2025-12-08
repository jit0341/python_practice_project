nums = [1, 2, 3, 4, 5]
for i in range(len(nums)):
    if nums[i] % 2 != 0:  # Check if the number is odd
        nums[i] = 0  #Replace all odd numbers in a list with 0
print(nums)
# Output: [0, 2, 0, 4, 0]

#Reverse a list using slicing.
my_list = [1, 2, 3]
reversed_list = my_list[::-1]
print(reversed_list)
# Output: [3, 2, 1]

#Create a new list with only the first letters of these words:
words = ["Python", "is", "fun"]
first_letters = [word[0] for word in words]
print(first_letters)
# Output: ['P', 'i', 'f']
