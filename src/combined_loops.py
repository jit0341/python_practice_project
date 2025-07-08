numbers = [1,7,12,3,10,8,15,20,5]
for num in numbers:
    if  num == 10:
    	print("Found the target number 10! Stopping search")
    	break
    if  num == 3:
    	print("Skipping lucky number 3!")
    	continue
    if num % 2 == 0:
    	print(f"Even number : {num}")
    else:
    	print(f"Odd number : {num}")
    	
    	