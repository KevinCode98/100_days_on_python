
#Step 2

import random
word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)

#Testing code
print(f'Pssst, the solution is {chosen_word}.')

#TODO-1: - Create an empty List called display.
#For each letter in the chosen_word, add a "_" to 'display'.
#So if the chosen_word was "apple", display should be ["_", "_", "_", "_", "_"] with 5 "_" representing each letter to guess.
display = ['_'] * len(chosen_word)
print(display)

end_of_game = False

while not end_of_game: 
    guess = input("Guess a letter: ").lower()
    for pos in range(len(chosen_word)):
        if guess == chosen_word[pos]:
            display[pos] = guess
        else:
            pass
    print(display)

    if "_" not in display:
        end_of_game = True
        print("You Win!")

#TODO-3: - Print 'display' and you should see the guessed letter in the correct position and every other letter replace with "_".
#Hint - Don't worry about getting the user to guess the next letter. We'll tackle that in step 3.

