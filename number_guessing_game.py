import random

def number_guessing_game():
    print("Welcome to the Number Guessing Game!")
    
    # Computer generates a random number between 1 and 100
    number_to_guess = random.randint(1, 100)
    attempts = 0
    guessed_correctly = False

    print("I have selected a number between 1 and 100. Try to guess it!")

    while not guessed_correctly:
        try:
            # User input
            guess = int(input("Enter your guess: "))
            attempts += 1
            
            # Check the guessed number
            if guess < number_to_guess:
                print("Too low! Try again.")
            elif guess > number_to_guess:
                print("Too high! Try again.")
            else:
                guessed_correctly = True
                print(f"Congratulations! You've guessed the number {number_to_guess} in {attempts} attempts.")
        
        except ValueError:
            print("Please enter a valid number.")

# Run the game
if __name__ == "__main__":
    number_guessing_game()
