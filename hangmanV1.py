import random

import word_lists
from  word_lists import athletes_list
from hangman_arts import hangman_arts


logo = r"""
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/    """

print(f"{'*' * 50}")
print(logo)
print(f"{'*' * 50} \n")


#TODO 1 - Generate random word from a wordlist  Randomly select an athlete's name



athletes_name = athletes_list()

# Initialize the current guessed state of the word. The container where letters will be placed one after the other
current_word_state = ["_"] * len(athletes_name) #display underscore, equal to the number of characters of the word
#This is a list of "_", that shows the length of the word

#TODO 2 - Generate dash lines to show the number of characters in the word




# TODO 3 - Code the Game loop

print(athletes_name)
print("_  " * len(athletes_name))  # Display underscores showing the length(number of chars) of the word

lives = 6

while True:
    guess_letter = input("\nEnter a letter: ").lower()  # Input a letter
    i = 1
    for index, letter in enumerate(athletes_name):
        if letter == guess_letter:
            current_word_state[index] = letter  # Reveal the guessed letter
    i += 1

    if guess_letter not in athletes_name:
        stages = hangman_arts(lives)
        print(f"Lives = {lives}")
        print(stages)
        lives -= 1
        print(f"You have {lives} Lives remaining!")


    mystery_word = (" ".join(current_word_state))
    print(mystery_word)
    print('*' * 50)
    word_len = len(athletes_name)
    if lives < 0:
        #print(stages)
        print("You Lose!")
        print(f"The correct word is {athletes_name.upper()}")
        print(f"You got {i} letters out of {word_len} letter word")
        exit()

    if "_" not in current_word_state:
        print("Congratulations! You Win!")
        yes_continue = input("Play again? (Y/N) ").lower()
        if yes_continue == "y":
            continue








