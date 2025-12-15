# Max min manual
nums = [5,9,1,7]
maxi = nums[0]
mini = nums[0]

for n in nums:
    if n > maxi:
        maxi = n
    if n < mini:
        mini = n

print("Max:", maxi)
print("Min:", mini)

