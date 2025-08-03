import random

low = int(input("Enter the lower range: "))
high = int(input("Enter the upper range: "))

number = random.randint(low, high)
guess = None

while guess != number:
    guess = int(input(f"Guess a number between {low} and {high}: "))
    if guess < number:
        print("Too low")
    elif guess > number:
        print("Too high")
    else:
        print("Correct! You guessed it.")
