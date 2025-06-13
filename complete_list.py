print("----1. List-type----")
my_list = [1,2,3]
print(my_list) 

print(type(my_list)) 

my_list2 = [1, 'Madhav', 'Keshav', True, 3.14]
print(my_list2) 
print(type(my_list2)) 


my_list3 = [1,2, [3,4] ,True, [5,6,7] ]
print(my_list3) 
print(type(my_list3))  


#Access list - Indexing 
print("----2.List Indexing-----")
list1 = [10, 20, 30, 40, 50]
# index: 0   1   2   3   4
# index:-5  -4  -3   -2  -1

# first element
print(list1[0])

# second element
print(list1[1])


# list - slicing 
print("-----3. List-slicing----")
list2 = [10, 20, 30, 40, 50, 60, 100]
# index: 0   1   2   3   4   5    6
# index: -7 -6  -5  -4  -3   -2  -1

# slicing syntax 
# list_name[start : stop : step]

# start is inclusive, default is 0
# stop is exclusive, default is -1/last index value 
 
# first 3 elements 
print("first 3 elements")
print(list2[0:3:1])

# elements from index 1 to 4
print("elements from index 1 to 4")
print(list2[1:5])

# last 3 elements 
print("Last 3 elements")
print(list2[-3:])

# alternative elements 
print("Alternative element")
print(list2[::2]) #step is 2 

# reverse list 
print("Reverse list")
print(list2[::-1]) #step is -1 


# last element
print("Last element")
print(list1[-1])

# second last element
print("Second last element")
print(list1[-2])  

# Middle 3 elements
print("Middle 3 elements")
print(list2[2:5])  # [30, 40, 50]

# First 4 elements reversed
print("First 4 elements reversed")
print(list2[3::-1])  # [40, 30, 20, 10]

# Copy list using slicing
print("Copy list using slicing")
copy_list = list2[:]
print(copy_list)     # Full copy of list2

# Length of list
print("Length of list2")
print(len(list2))  # Output: 7

# Membership test
print("Is 40 in list2?")
print(40 in list2)  # True

# Count occurrences
print("Count of 10 in list2")
print(list2.count(10))  # 1

# Index of an element
print("Index of 50 in list2")
print(list2.index(50))  # 4