fruits = ['apple', 'banana', 'cherry', 'date', 'fig', 'grape']
# Index:     0        1         2       3     4      5
# NegIndex: -6       -5        -4      -3    -2     -1
print(fruits[1:4])      # ['banana', 'cherry', 'date']
print(fruits[:3])       # ['apple', 'banana', 'cherry']
print(fruits[3:])       # ['date', 'fig', 'grape']
print(fruits[:])        # Full copy: ['apple', 'banana', 'cherry', 'date', 'fig', 'grape']
print(fruits[-3:])      # ['date', 'fig', 'grape']
print(fruits[-4:-1])    # ['cherry', 'date', 'fig']
print(fruits[-4:-2])   # ['cherry','date']
print(fruits[-5:-1])     #(banana to fig)

print(fruits[::2])      # ['apple', 'cherry', 'fig'] (every 2nd item)
print(fruits[1::2])     # ['banana', 'date', 'grape']
print(fruits[1::1])   # All items except first.
print(fruits[::3])   # every 3rd item

print(fruits[::-1])     # ['grape', 'fig', 'date', 'cherry', 'banana', 'apple'] (reversing)
print(fruits[::-2])  # reverse every 2nd item
