import random

import word_lists
from  word_lists import athletes_list
from hangman_arts import hangman_arts

#def start_hangman():

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
word_len = len(athletes_name)

# Initialize the current guessed state of the word. The container where letters will be placed one after the other
current_word_state = ["_"] * len(athletes_name) #display underscore, equal to the number of characters of the word
#This is a list of "_", that shows the length of the word

#TODO 2 - Generate dash lines to show the number of characters in the word

# TODO 3 - Code the Game loop
lives_on = 6


print("Welcome to Hangman Game. You will be askes to guess letters of a word. In this case names of world athletes")
print(f"Guess a {word_len} letter name of a world athlete")
i = 0
cont = True
while cont:
    print("\n" + athletes_name)
    print("_  " * len(athletes_name))  # Display underscores showing the length(number of chars) of the word
    guess_letter = input("\nEnter a letter: ").lower()  # Input a letter

    for index, letter in enumerate(athletes_name):
        if letter == guess_letter:
            i += 1
            current_word_state[index] = letter  # Reveal the guessed let


    print(i)
    if guess_letter not in athletes_name:
        stages = hangman_arts(lives_on)
        print(f"Lives = {lives_on}")
        print(stages)
        print(f"You have {lives_on} Lives remaining!")
        lives_on -= 1

    mystery_word = (" ".join(current_word_state))
    print(mystery_word)
    print('*' * 50)
    word_len = len(athletes_name)

    if lives_on < 0:
        print("You Lose!")
        print(f"The correct word is {athletes_name.upper()}")
        print(f"You got {i} letter(s)out of {word_len} letter word")

        ans = input("Continue? Y/N? ").lower()

        if ans == "y":
            continue
        else:
            cont = False

    if "_" not in current_word_state:
        print("Congratulations! You Win!")
        ans = input("Continue? Y/N? ").lower()

        if ans == "y":
            continue
        else:
            cont = False









