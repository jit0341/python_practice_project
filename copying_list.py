print("\n--- 7. Copying Lists ---")
original_list = [1, 2, 3]

# Method 1: Assignment (creates a reference, NOT a copy)
reference_list = original_list
reference_list.append(4)
print(f"Original after reference modify: {original_list}") # Output: Original after reference modify: [1, 2, 3, 4] (modified!)
print(f"Reference list: {reference_list}") # Output: Reference list: [1, 2, 3, 4]