## Checks if a number is prime
# or composite.

(f"{num} is neither prime nor composite")
    else:
        is_prime = True
        i = 2
        while i < num:
            if num % i == 0:
                is_prime = False
                break
            i += 1

        if is_prime:
            print(f"{num} is a Prime number")
        else:
            print(f"{num} is a Composite number")
    
    num += 1
