secret_number = 7
guess = 0
attempts = 0

while guess != secret_number and attempts < 3:
    guess = int(input("Guess the number: "))
    attempts += 1
    
    if guess == secret_number:
        print("Congratulations! You guessed it right.")
    else:
        print("Wrong guess. Try again!")

if guess != secret_number:
    print("Sorry! You’ve used all your attempts.")
