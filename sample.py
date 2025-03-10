import random

print("Game to Guess the Number!")

# Generate a random number between 1 and 50
number_to_guess = random.randint(1, 50)

# Ask user for input
inputnum = int(input("Enter your desired number (Between 1 to 50): "))

# Check if input is within range
if inputnum < 1 or inputnum > 50:
    print(f"Kindly enter a number between 1 and 50 only. Your input: {inputnum}")
else:
    print("Let's begin the game!")

    while inputnum != number_to_guess:
        if inputnum < number_to_guess:
            print("Wrong input! Try a **higher** number.")
        else:
            print("Wrong input! Try a **lower** number.")

        # Ask user for a new guess
        inputnum = int(input("Enter a new number: "))

    # If user guesses correctly, exit loop and print success message
    print(f"Congratulations! You guessed the correct number: {number_to_guess}")