def show_game_logo():
    print('''
            *******************************************************************************
                      |                   |                  |                     |
             _________|________________.=""_;=.______________|_____________________|_______
            |                   |  ,-"_,=""     `"=.|                  |
            |___________________|__"=._o`"-._        `"=.______________|___________________
                      |                `"=._o`"=._      _`"=._                     |
             _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
            |                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
            |___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
                      |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
             _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
            |                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
            |___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
            ____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
            /______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
            ____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
            /______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
            ____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
            /______/______/______/______/______/______/______/______/______/______/[TomekK]
            *******************************************************************************
            ''')

def ask_to_continue():
#while True:
    choice = input("Do you want to continue? Yes/No ").title()
    if choice == "Yes":
        play_game()
        #return True
    elif choice == "No":
        #break
        return False
    else:
        print("Please enter Yes or No: ")

def new_path():
    door_color = input("Which door would you like to go? Red, Blue, Yellow? \n").title()
    if door_color == "Red":
        print(" You were burned by fire! Game Over!! \n")

    elif door_color == "Blue":
        print(" You were eaten by a beast! Game Over!! \n")

    elif door_color == "Yellow":
        print("You Win! \n \n")
        return ask_to_continue()

    else:
        print("Game Over!!! \n \n")
    return ask_to_continue()

def handle_left_move():
    move2 = input("Do you want to swim or wait? ").title()
    if move2 == "Swim":
        print("You were attacked by an aligator! Game Over!! \n \n")
        return ask_to_continue()
    elif move2 == "Wait":
        return new_path()
        #return True  # Continue game with next scenario
    else:
        print("\nInvalid choice. Please choose 'swim' or 'wait'.")
        return True  # Give player another chance


def play_game():
    while True:
        print("Welcome to my Treasure Island")
        print("Your mission is to find the treasure")
        move_choice = input("Where do you want to go? Left or Right? \n").title()
        if move_choice == "Left":
            if not handle_left_move():
                break
        elif move_choice == "Right":
            print("You fall into a hole. Game Over!! \n")
            pass
        else:
            print("Please choose 'Left' or 'Right': ")

print("Bye!")

show_game_logo()

play_game()