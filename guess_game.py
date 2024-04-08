import sys
from random import randint
from functions import get_int, get_int_within_range
from math import log2 


def main():
    print("Choose a number range. (The first input is the lower bound and the second is the higher bound)")

    # Guess lower and upper bound
    lower = get_int("Lower bound: ")
    upper = get_int("Higher bound: ")

    # Ensure the range of numbers is greater than 10 
    while upper - lower < 10:
        print("Range of numbers too low.")

        lower = get_int("Lower bound: ")
        upper = get_int("Higher bound: ")

    # Randomly chosen number
    computer_number = randint(lower, upper)

    # Number of guesses
    count = 0

    # Maximum number of guesses allowed
    maximum_guess = int(log2(upper - lower + 1))

    print(f"You have {maximum_guess} guesses to play this game")

    # While the user hasn't reached the maximum number of guesses
    while count < maximum_guess:
        count += 1
        user_input_guess = get_int_within_range("Choose a number: ", lower, upper)

        if user_input_guess > computer_number:
            print("Guessed too high")
        elif user_input_guess < computer_number:
            print("Guessed too low")
        else:
            print(f"Congratulations! You guessed the correct number: {computer_number} in {count} guesses.")
            sys.exit()

    # If the user reaches the maximum number of guesses without guessing the correct number
    print("You have reached the maximum number of guesses. The correct number was:", computer_number)

if __name__ == "__main__":
    main()
