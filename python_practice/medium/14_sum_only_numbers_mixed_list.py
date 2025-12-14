# Mixed list: Only numbers sum
items = [10,'a', 20, 'hello',30]
total = 0
for i in items:
    if type(i) == int:
        total += i
        print(total)

