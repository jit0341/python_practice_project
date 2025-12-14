from statistics import mean, median, mode, stdev # Good practice to import specifically
# Or from statistics import * # As shown in the repo example

ages = [20, 20, 4, 24, 25, 22, 26, 20, 23, 22, 26]
print(f"Ages: {ages}")
print(f"Mean: {mean(ages)}")
print(f"Median: {median(ages)}")
print(f"Mode: {mode(ages)}")
print(f"Standard Deviation: {stdev(ages):.2f}")
