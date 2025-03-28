import art
import random

# generates list
numbers = list(range(1,101))

def generate_number():
    """returns a random number"""
    return random.choice(numbers)

def pick_level ():
    """prompts user for difficulty, and returns attempts No"""
    level = int(input("Choose a difficulty. Type 1 for easy or 2 for hard: "))
    # easy
    if level == 1:
        return  10
    # hard
    elif level == 2:
        return 5
    else:
        print("Invalid choice. Difficulty set to easy.")
        return 10

# returns high or low
def analyze(guess, chosen_number, attempts):
    """evaluates  and prints if user's guess is too high or low, decreasing the remaining_attempts"""

    if guess > chosen_number:
        print("Too high.")

    if guess < chosen_number:
        print("Too low.")


def play():
    chosen_number = generate_number()

    # initial texts
    print(art.logo)
    print("Welcome to the Guess The Number Game!")
    print("I'm thinking of a number between 1 and 100.")
    attempts = pick_level()

    while attempts > 0:
        try:
            guess = int(input("Make a guess: "))
        except ValueError:
            print("Please enter a valid number.  ")
            continue

        # right answer
        if guess == chosen_number:
            print(f"Congrats! You won, the chosen number was {chosen_number}.")
            return
        # wrong answer
        if guess != chosen_number:
            analyze(guess,chosen_number, attempts)
            attempts -= 1
            print(f"You have {attempts} attempts remaining to guess the number. ")

        # if attempts ran out
        if attempts == 0:
            print("You've run out of guesses. Refresh the page to run again.")
            break

play()


