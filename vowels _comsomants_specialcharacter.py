## Here’s a small Python program 
# that combines conditionals, 
loops, and strings.A more
# advanced version that also counts
# digits, spaces, and special 
# characters along with vowels
# and consonants:

word = input("Enter a sentence: ")
vowels = "aeiouAEIOU"
vowel_count = 0
consonant_count = 0
digit_count = 0
space_count = 0
special_count = 0

for char in word:
    if char.isalpha():
        if char in vowels:
            vowel_count += 1
        else:
            consonant_count += 1
    elif char.isdigit():
        digit_count += 1
    elif char.isspace():
        space_count += 1
    else:
        special_count += 1

print("Vowels:", vowel_count)
print("Consonants:", consonant_count)
print("Digits:", digit_count)
print("Spaces:", space_count)
print("Special Characters:", special_count)
