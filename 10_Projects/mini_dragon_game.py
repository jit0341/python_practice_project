## A small text-based or console
# game, possibly involving a dragon
# or similar theme.

import random

# Give your dragon a name
your_name = input("Name your dragon: ")
your_power = random.randint(50, 100)

# Enemy dragon
enemy_name = "Shadowfang"
enemy_power = random.randint(50, 100)

# Show stats
print("\nBattle Begins!")
print(your_name, "Power:", your_power)
print(enemy_name, "Power:", enemy_power)

# Decide winner
if your_power > enemy_power:
