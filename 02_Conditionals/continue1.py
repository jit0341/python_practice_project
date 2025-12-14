fruits = ["Apple", "Banana", "Cherry", "Date", "Elderberry"]

for fruit in fruits:
    if fruit == "Banana":
        continue  # Skips to the next iteration if fruit is "Banana"

    # This line will only be reached if 'fruit' was NOT "Banana"
    print(f"I like {fruit}!") # Corrected f-string syntax

       