secret_number = 7
guess = 0

while guess != secret_number:
    guess = int(input("Guess the number: "))
    if guess == secret_number:
        print("Congratulations! You guessed it right.")
    else:
        print("Try again!")
