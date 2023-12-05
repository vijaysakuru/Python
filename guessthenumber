import random

def guess_the_number():
    # Set the range for the random number
    lower_bound = 1
    upper_bound = 100

    # Generate a random number within the range
    secret_number = random.randint(lower_bound, upper_bound)

    print(f"Guess the number! It's between {lower_bound} and {upper_bound}.")

    attempts = 0

    while True:
        attempts += 1
        try:
            # Get the player's guess
            guess = int(input("Enter your guess: "))

            # Check if the guess is correct, too high, or too low
            if guess == secret_number:
                print(f"Congratulations! You've guessed the number in {attempts} attempts.")
                break
            elif guess < secret_number:
                print("Too low! Try again.")
            else:
                print("Too high! Try again.")
        except ValueError:
            print("Please enter a valid number.")

if __name__ == "__main__":
    guess_the_number()
