import random

# Rock
rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

# Paper
paper ="""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

# Scissors
scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""
game_images = [rock, paper, scissors]
'''
print("0. Rock wins against scissors")
print("1. Paper wins against rock")
print("2. Scissors wins against paper")

'''


while True:
    users_choice = int(input("\nType 0 for Rock, 1 for Paper and 2 for Scissors: "))
    #print(users_choice)
    if users_choice == 0:
        users_choice_description = "Rock"
    elif users_choice == 1:
        users_choice_description = "Paper"
    elif users_choice == 2:
        users_choice_description = "Scissors"

    computer_choice = random.randint(0,2)

    if computer_choice == 0:
        computer_choice_description = "Rock"
    elif computer_choice == 1:
        computer_choice_description = "Paper"
    elif computer_choice == 2:
        computer_choice_description = "Scissors"

    print(game_images[users_choice])
    print(users_choice_description)

    print(game_images[computer_choice])
    print(computer_choice_description)
    print(f"\n User's Choice: {users_choice}-{users_choice_description}, Computer's Choice: {computer_choice}-{computer_choice_description}")

    valid_choices = [0, 1, 2]


    if users_choice in valid_choices:
        if users_choice == computer_choice:
            print("It's a Draw!...You Lose!")
        elif users_choice == 0 and computer_choice == 2:
            print("Rock wins against scissors. You win!..")
        elif users_choice > computer_choice:
            print(f" {users_choice_description} wins against {computer_choice_description}! You win!..")
        elif users_choice < computer_choice:
            print(f"{computer_choice_description} wins against {users_choice_description}! You Lose!..")
    else:
        print("You typed an invalid choice!..")



