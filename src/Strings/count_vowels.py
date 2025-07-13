## Program: Count vowels in a word

word = input("Enter a word: ")
vowels = "aeiouAEIOU"
count = 0

for char in word:
    if char in vowels:
        count += 1

print("Number of vowels:", count)
