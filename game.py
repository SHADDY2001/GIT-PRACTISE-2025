import random

print("🎮 Welcome to the Number Guessing Game! 🎮")
print("I'm thinking of a number between 1 and 20. Can you guess it?")

# Generate random number
number = random.randint(1, 20)
attempts = 0

while True:
    guess = input("Enter your guess: ")

    # Check if input is a number
    if not guess.isdigit():
        print("❌ Please enter a valid number.")
        continue

    guess = int(guess)
    attempts += 1

    if guess < number:
        print("📉 Too low! Try again.")
    elif guess > number:
        print("📈 Too high! Try again.")
    else:
        print(f"🎉 Congrats! You guessed it in {attempts} attempts.")
        break
