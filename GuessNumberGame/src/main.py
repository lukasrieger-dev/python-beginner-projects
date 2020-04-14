# Guess Random Number Game
import random

__author__ = 'codinglukas'


MAX_NUMBER = 100
secret_number = random.randint(0, MAX_NUMBER)
rounds = 1

print(f"Can you guess my secret number? Its between 0 and {MAX_NUMBER}")

while True:
    guess_str = input("Guess my number: ")
    try:
        guess = int(guess_str)
    except ValueError:
        print(f"Enter a number between 0 and {MAX_NUMBER}")
        continue

    if guess == secret_number:
        print("YES, THAT IS MY SECRET NUMBER!")
        break

    if guess > secret_number:
        print("NO, MY SECRET NUMBER IS SMALLER.")
    else:
        print("NO, MY SECRET NUMBER IS BIGGER.")
    rounds += 1

print(f">>> YOU FOUND MY SECRET NUMBER AFTER {rounds} GUESSES.")
