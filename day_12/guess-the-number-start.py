from art import logo
import random
#Number Guessing Game Objectives:
HARD_LEVEL = 5
EASY_LEVEL = 10


# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).
def set_difficulty():
    chose = input("Choose a difficulty. Type 'easy' or 'hard': ")
    return EASY_LEVEL if chose == 'easy' else HARD_LEVEL

def check_answare(guess, answer, turn):
    if guess > answer:
        print("Too high")
        return turn - 1

    elif guess < answer:
        print("To low")
        return turn -1
    else:
        print(f"You got it! The asware was {answer} :)")

def game():
    print(logo)
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    answer = random.randint(1,100)
    
    turns = set_difficulty()

    guess = 0

    while guess != answer:
        print(f"You have {turns} attempts remaining to guess the number.")
        guess = int(input("Make a guess: "))
        turns = check_answare(guess, answer,turns)

        if turns == 0:
            print("You've run out of guesses, You lose! :(")
        elif guess != answer:
            print("Guess again!")

game()
