## This program counts both vowels
# and consonants in a word.

word = input("Enter a word: ")
vowels = "aeiouAEIOU"
vowel_count = 0
consonant_count = 0

for char in word:
    if char.isalpha():  # Check if it's a letter
        if char in vowels:
            vowel_count += 1
        else:
            consonant_count += 1

print("Vowels:", vowel_count)
print("Consonants:", consonant_count)
