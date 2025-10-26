# number_guessing_game.py
# Author: Your Name
# Date: October 2025
# Description: A simple number guessing game for Hacktoberfest 🎃
# The program randomly picks a number, and the user tries to guess it.

import random

def play_game():
    """
    Plays the number guessing game.
    """
    print("🎯 Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100...")
    
    secret_number = random.randint(1, 100)
    attempts = 0

    while True:
        try:
            guess = int(input("Enter your guess: "))
            attempts += 1

            if guess < secret_number:
                print("📉 Too low! Try again.")
            elif guess > secret_number:
                print("📈 Too high! Try again.")
            else:
                print(f"🎉 Correct! The number was {secret_number}.")
                print(f"You guessed it in {attempts} attempts!")
                break
        except ValueError:
            print("⚠️ Please enter a valid number.")

def main():
    while True:
        play_game()
        play_again = input("Play again? (y/n): ").lower()
        if play_again != "y":
            print("👋 Thanks for playing! Goodbye!")
            break

if __name__ == "__main__":
    main()
