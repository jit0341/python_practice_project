Numbers = [1,7,12,3,10,8,15,20,5] # List is correctly defined
for num in Numbers:              # CORRECT: Iterating directly over the list!
    if  num == 10:               # CORRECT: Checks for 10 and applies break.
    	print("Found the target number 10! Stopping search")
    	break
    if  num == 3:                # CORRECT: Checks for 3 and applies continue.
    	print("Skipping lucky number 3!")
    	continue
    # CORRECT: These checks are only reached if num was not 10 or 3.
    if num % 2 == 0:
    	print(f"Even number : {num}")
    else:
    	print(f"Odd number : {num}")
