# Number Guessing Game
import random

print("Welcome to the Guess the number game!")

# Will randomly pick a number between 1-100
answer = random.randrange(1,100)

while True:
    guess = int (input("Please guess a number between 1-100! "))

    if (guess == answer):
        print('Congrats the you guessed the correct number! ')
        break

    elif (guess > answer):
        print("Not quite! your guess was too high! Please guess again!")
    
    elif (guess < answer):
        print("Not quite! your guess was too low! Please guess again!")
    

