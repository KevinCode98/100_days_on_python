rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line ??
import random
list_choice = {0:rock, 1:paper, 2:scissors}
computer_choice = random.randint(0,2)
user_choice = int(input("Wha do you chose? Type 0 for rock, 1 for Paper or 2 for Scissors.\n"))

print(f'Computer chose {list_choice[computer_choice]}')
print(f'You chose {list_choice[user_choice]}')

if computer_choice == user_choice:
    print('Draw!')

elif user_choice == 0:
    if computer_choice == 1:
        print('You lose')
    else:
        print('You win!')

elif user_choice == 1:
    if computer_choice == 2:
        print('You lose')
    else:
        print('You win')

elif user_choice == 2:
    if computer_choice == 0:
        print('You lose')
    else:
        print('You win')
