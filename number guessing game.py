import random

print("Welcome to Monika's Number Guessing Game!")

# Step 1: Generate a random secret number between 1 and 10
secret_number = random.randint(1, 10)

# Step 2: Keep track of attempts
attempts = 0

# Step 3: Loop until the player guesses correctly
while True:
    guess = int(input("Guess a number between 1 and 10: "))
    attempts += 1   # count each guess

    if guess == secret_number:
        print("🎉 Correct! You guessed it in", attempts, "attempts.")
        break   # exit the loop when guessed correctly
    elif guess < secret_number:
        print("Too low, try again!")
    else:
        print("Too high, try again!")
