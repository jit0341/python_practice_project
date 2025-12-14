numbers = [0,1,2,3,4,5,6,7,8,9]
print(f"Even numbers(step2):{numbers[0::2]}")
print(f"Odd numbers(step3):{numbers[1::2]}")
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

even_numbers = [num for num in numbers if num % 2 == 0]
odd_numbers = [num for num in numbers if num % 2 != 0]

print(f"Even numbers (by value): {even_numbers}")
print(f"Odd numbers (by value): {odd_numbers}")
