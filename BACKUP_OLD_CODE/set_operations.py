my_set = {1, 2, 3}
empty_set = set()  # ❗ not {} (that’s a dict)
my_set.add(4)
my_set.update([5, 6, 7, 8])
my_set.remove(3)   # ❌ Error if 3 not present
my_set.discard(10) # ✅ No error if 10 not present
my_set.pop()       # Removes a random element
len(my_set)
3 in my_set       # True or False
for item in my_set:
    print(item)
    
    
    
A = {1, 2, 3, 4}
B = {3, 4, 5, 6}

print("Union:", A | B)
print("Intersection:", A & B)
print("Difference A - B:", A - B)
print("Symmetric Difference:", A ^ B)



numbers = {1, 2, 3, 2, 4, 3, 5}
print(numbers)

numbers.add(6)
numbers.remove(1)
numbers.discard(10)
print("Final set:", numbers)


X = {10, 20, 30}
Y = {30, 40, 50}

print(X & Y)
print(X ^ Y)
X.update(Y)
print(X)