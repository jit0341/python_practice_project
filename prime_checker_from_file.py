# Prime number checker from file

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

try:
    with open('numbers.txt', 'r') as file:
        for line in file:
            line = line.strip()
            if line == '' or line.startswith('#'):
                continue  # skip blank or comment lines
            try:
                num = int(line)
            except ValueError:
                print(f"Skipping invalid line: {line}")
                continue
            if is_prime(num):
                print(f"{num} is a prime number")
            else:
                print(f"{num} is not a prime number")

except FileNotFoundError:
    print("❌ File 'numbers.txt' not found. Please make sure it exists in the same folder.")
