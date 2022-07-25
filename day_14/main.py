from art import logo, vs
from game_data import data
import random

# Display art
print(logo)
score = 0

def format_data(account):
    """
    Takes the account data and returns the printable format.
    """
    account_name = account["name"]
    account_desc = account["description"]
    account_country = account["country"]
    return f"{account_name},  a {account_desc}, from {account_country}"


def check_answer(guess, a_followers, b_followers):
    """
    Take the user guess and follower counts and returns if they got it right.
    """
    if a_followers > b_followers:
        return guess == 'a'
    else:
        return  guess == 'b'

account_b = random.choice(data)

while True:
    # Generate a random account from the game data.
    account_a = account_b 
    account_b = random.choice(data) 

    if account_a == account_b:
        account_b = random.choice(data)

    print(f"Compare A: {format_data(account_a)}.")
    print(vs)
    print(f"Compare B: {format_data(account_b)}.")

    # Ask user for a guess.
    guess = input("Who has more followers? Type 'A' or 'B': ").lower()

    # Check if user is correct
    ## Get follower count of each account   
    a_follower_acount = account_a["follower_count"]
    b_follower_acount = account_b["follower_count"]

    is_correct = check_answer(guess, a_follower_acount, b_follower_acount)

    ## Use if statement to check if user is correct.
    if is_correct:
        score += 1
        print(f"You're right! Current score: {score}")
    else:
        print(f"Sorry, that's wrong. Final score: {score}")
        break

# Give user feedback on their guess.

# Score keeping.

# Make the game repeatable. 

# Making account at position B become the next account at position A.

# Clear the screen between rounds.
