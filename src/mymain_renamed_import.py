# mymain_renamed_import.py

# Renaming imports for clarity or to avoid conflicts
from mymodule import generate_full_name as fullname, sum_two_nums as total, \
                     gravity as g, person as p

# Test fullname (aliased generate_full_name)
print(f"Full name (aliased): {fullname('Asabneh', 'Yetegeg')}") # Added a last name for completeness

# Test total (aliased sum_two_nums)
print(f"Total of 1 and 9: {total(1, 9)}")

# Test g (aliased gravity)
mass = 100
weight = mass * g
print(f"Weight of 100kg object (aliased gravity): {weight:.2f} Newtons")

# Test p (aliased person)
print(f"Person's first name (aliased): {p['firstname']}")
