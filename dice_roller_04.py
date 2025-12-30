import random

# This program simulates a dice rolling game where the user guesses a number
print("Welcome to the Dice Roller!")

# Ask the user for their name
name = input("What's your name?: ")

# Ask the user to guess a dice number between 1 and 10
number = float(input("Enter your expected Dice Number [1-10]: "))

# Generate a random number between 1 and 10 for the computer
computerrandom = random.randint(1, 10)

# Check if the user's guess matches the computer's random number
if number == computerrandom:
    print(f"congratulation, {name} here's your guess {number} and here's the machine random output {computerrandom}")
else:
    print(f"You lose, {name} here's your guess {number} and here's the machine random output {computerrandom}")
