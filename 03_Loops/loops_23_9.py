fruits = ["Apple","Orange","Banana","Cherry","Peach"]

for fruit in fruits:
    if fruit == "Banana":
        continue

    print(f"I love {fruits}")


for nums in range(1,11):
    if nums % 3 == 0:
        print("Skipping a multiple of 3!")
        continue
    print(f"Current number is {nums}")

