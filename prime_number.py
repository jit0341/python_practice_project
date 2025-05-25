# Output Screenshot:
# ![Prime Number Output](prime_number_output.png)
while num <= 100:
    is_prime = True  # Assume number is prime

    i = 2
    while i < num:
        if num % i == 0:
            is_prime = False
            break  # Not a prime number
        i += 1

    if is_prime:
        print(f"{num} is a prime number")
    num += 1
