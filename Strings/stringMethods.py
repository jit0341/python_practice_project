# 1.
sentence = "this is a test sentence."
print(sentence.capitalize()) # Output: This is a test sentence.

headline = "the quick brown fox jumps over the lazy dog"
print(headline.title())    # Output: The Quick Brown Fox Jumps Over The Lazy Dog

# 2.
my_string = "Hello World"
new_string = my_string.upper() # my_string remains "Hello World"
                                # new_string becomes "HELLO WORLD"

print(my_string) # Output: Hello World
print(new_string) # Output: HELLO WORLD

# 3.
padded_text = "   Hello World   "
print(padded_text.strip())  # Output: "Hello World"
print(padded_text.lstrip()) # Output: "Hello World   "
print(padded_text.rstrip()) # Output: "   Hello World"

# You can also specify characters to remove
weird_string = "###Data###"
print(weird_string.strip('#')) # Output: "Data"
