a = "hello world"
print(a[::-1])   #slicing
print(a[1:4])
print(a[3:9])
print(a[0:4])

#in-place swapping
a = 10
b = 5
a,b = b,a
print(f"a:{a},b:{b}")

# Generator
my_generator = (x*2 for x in range(10))
print(my_generator)

for val in my_generator:
	print(val)
	
even_gen = (x for x in range(0,21,2))
for num in even_gen:
	print(num,end= " ")
	
print()
print("-"*40)
squares = (n*n for n in range(1,11))
print(list(squares))


