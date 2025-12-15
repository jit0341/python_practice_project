# String starting with vowels
words = ['apple','dog','elephant','cat','eyes']
vowels ='aeiou'
for w in words:
    if w[0].lower() in vowels:
        print(w)
