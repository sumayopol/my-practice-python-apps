import random

# Import word list and hangman art
from word_lists import athletes_list
from hangman_arts import hangman_arts

# Logo for Hangman
logo = r"""
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/    """

cont = True

while cont:
    print(f"{'*' * 50}")
    print(logo)
    print(f"{'*' * 50} \n")

    # Game Introduction
    print("Welcome to the Hangman Game!")
    print("Guess the name of a world-class athlete, one letter at a time.")

# Game Loop

    # Randomly select a word from athletes_list
    athletes_name = athletes_list().lower()
    word_len = len(athletes_name)

    # Initialize guessed letters and lives
    current_word_state = ["_"] * word_len
    lives_on = 7
    guessed_letters = []

    print(f"Guess a {word_len}-letter name of a world athlete.")

    # Game loop for a single round
    while lives_on >= 0:

        print(athletes_name)

        # Display the current state of the word
        print("\n" + " ".join(current_word_state))

        # Input a guess from the player
        guess_letter = input("Enter a letter: ").lower()

        # Check for repeated guesses
        if guess_letter in guessed_letters:
            print("You already guessed that letter. Try again.")
            continue
        guessed_letters.append(guess_letter)

        # Update the current word state if the guess is correct
        if guess_letter in athletes_name:
            for index, letter in enumerate(athletes_name):
                if letter == guess_letter:
                    current_word_state[index] = letter
            print("Correct guess!")
        else:
            print("Wrong guess!")
            lives_on -= 1
            stages = hangman_arts(lives_on)
            print(stages)# Show the hangman art
            print(f"Lives remaining: {lives_on}")

        # Check for win condition
        if "_" not in current_word_state:
            print("\nCongratulations! You guessed the word!")
            print(f"The word was: {athletes_name.upper()}")
            break


        # Check for lose condition
        if lives_on == 0:
            print("\nYou lose!")
            print(f"The correct word was: {athletes_name.upper()}")
            break

    # Ask the player if they want to continue
    ans = input("Do you want to play again? (Y/N): ").lower()
    if ans != "y":
        cont = False
        print("Thanks for playing Hangman!")
