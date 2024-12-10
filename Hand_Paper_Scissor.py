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


while True:
    human_choice = int(input("\n Type '0' for rock, '1' for paper and '2' for scissors: "))

    valid_choices = [0, 1, 2]
    if human_choice in valid_choices:

        if human_choice == 0:
            print(rock)
            print(f"\n User's Choice: Rock - {human_choice} ")
        elif human_choice == 1:
            print(paper)
            print(f"\n User's Choice: Paper - {human_choice} ")
        elif human_choice == 2:
            print(scissors)
            print(f"\n User's Choice: Scissors - {human_choice} ")

        #print(f"\n User's Choice:  {users_choice} ")
    comp_choice = random.randint(0,2)


    if comp_choice == 0:
        print(rock)
        print(f"\n Computer's Choice: Rock - {comp_choice} ")
    elif comp_choice == 1:
        print(paper)
        print(f"\n Computer's Choice: Paper - {comp_choice} ")
    elif comp_choice == 2:
        print(scissors)
        print(f"\n Computer's Choice: Scissors - {comp_choice} ")


    print(f" \n User's Choice : {human_choice} Computer's Choice: {comp_choice} ")
    #print("\n '0' for rock, '1' for paper and '2' for scissors: ")
    print("0. Rock wins against scissors")

    print("1. Scissors wins against paper")

    print("2. Paper wins against rock")
    print()
    #print(f" Computer Choice: {comp_choice} ")


    if human_choice == comp_choice:
        print("\n      It's a Draw! You lose..")

    elif (human_choice == 0 and comp_choice == 2) or (human_choice == 1 and comp_choice == 0) or (human_choice == 2 and comp_choice == 1):
        print("   You Win!..")

    elif (human_choice == 2 and comp_choice == 0) or (human_choice == 0 and comp_choice == 1) or (human_choice == 1 and comp_choice == 2):
        print("   You Lose!..")

    else:
        again = input("Invalid Choice! Play again? Yes/No: ").title()
        if again == "Yes":
            continue


