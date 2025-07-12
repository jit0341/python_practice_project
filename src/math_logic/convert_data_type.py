#Converting one data type to another data type

#int to float
num_int = 10
print('num_int',num_int)         # 10
num_float = float(num_int)
print('num_float:', num_float)   # 10.0

# float to int
gravity = 9.81
print(int(gravity))             # 9

# int to str
num_int = 10
print(num_int)                  # 10
num_str = str(num_int)
print(num_str)                  # '10'

# str to int or float
num_str = '10.6'
num_float = float(num_str)
print('num_float', float(num_str))  # 10.6
num_int = int(num_float)
print('num_int', int(num_int))      # 10

# str to list
first_name = 'Jitendra'
print(first_name)               # 'Asabeneh'
first_name_to_list = list(first_name)
print(first_name_to_list)            # ['A', 's', 'a', 'b', 'e', 'n', 'e', 'h']

# str to tuple
first_name_to_tuple = tuple(first_name)
print(first_name_to_tuple)
# output ('J', 'i', 't', 'e', 'n', 'd', 'r', 'a')

# str to set
first_name_to_set = set(first_name)
print(first_name_to_set)
 # {'r', 'e', 'd', 'i', 't', 'n', 'a', 'J'}
help()