import random

while True:
    try:
        secret_number = random.randint(1, 10)
        maximum_attempts = 3
        attempts = 0
        while attempts < maximum_attempts:
            attempts += 1
            guess = int(input("Guess a number between 1 and 10: "))
            if guess == secret_number:
                print(f"Congratulations! You won in {attempts} attempts")
                break
            elif guess < secret_number:
                print("Too Low! Try again")
            elif not 1 <= guess <= 10:
                print("Invalid input: Enter a number within the specified range.")
            else:
                print("Too high: Try again")
    except ValueError:
        print("Invalid input: Enter a valid number")




