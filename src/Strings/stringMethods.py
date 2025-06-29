# 1. capitalize(), title()
sentence = "this is a test sentence."
print(sentence.capitalize()) # Output: This is a test sentence.

headline = "the quick brown fox jumps over the lazy dog"
print(headline.title())    # Output: The Quick Brown Fox Jumps Over The Lazy Dog

# 2. upper(), lower()
my_string = "Hello World"
new_string = my_string.upper() # my_string remains "Hello World"
                                # new_string becomes "HELLO WORLD"

print(my_string) # Output: Hello World
print(new_string) # Output: HELLO WORLD

# 3. strip(), lstrip(), rstrip()
padded_text = "   Hello World   "
print(padded_text.strip())  # Output: "Hello World"
print(padded_text.lstrip()) # Output: "Hello World   "
print(padded_text.rstrip()) # Output: "   Hello World"

# You can also specify characters to remove
weird_string = "###Data###"
print(weird_string.strip('#')) # Output: "Data"

# 4. find() and index()
phrase = "The quick brown fox"
print(phrase.find("quick")) # Output: 4 (index where 'q' is found)
print(phrase.find("dog"))   # Output: -1

print(phrase.index("quick")) # Output: 4
# print(phrase.index("dog")) # This would raise a ValueError

# 5. replace()
greet = "Hello World"
print(greet.replace("World", "Python")) # Output: Hello Python
print(greet.replace("l", "X"))          # Output: HeXXo WorXd


# 6. split()
data = "apple,banana,orange"
fruits = data.split(',')
print(fruits) # Output: ['apple', 'banana', 'orange']

sentence = "This is a sample sentence"
words = sentence.split() # Splits by whitespace by default
print(words) # Output: ['This', 'is', 'a', 'sample', 'sentence']

