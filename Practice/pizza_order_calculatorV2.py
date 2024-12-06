'''
Development approach
1. Study the entire pizza order process
    - User orders pizza ->(pizza_order()
    - App provides pizza options(size, with pepperoni, with cheese) -> pizza_description()
    - App calculates total price of the order -> compute_order()
2. Description of available products
3. Computation of pizza orders

'''

def compute_order(size, pepperoni, cheese): # the function compute_order receives 3 parameters from the pizza_order function
    #creates a dictionary (price) of pizza sizes and corresponding price
    price = {
        "S":15,
        "M":20,
        "L":25
    }

    # The basic price of a pizza according to it size, is expressed this way
    total = price[size]


    if pepperoni == "Y": #if the user orders an extra pepperoni and if the size is small add 2 to total and 3 if the size is large and medium
        if size =="S":
            total += 2
        else:
            total += 3

    if cheese == "Y": #if user orders an extra cheese, he will be charged 1 for all sizes
        total += 1

    return total # the function returns the total order price of the pizza.


def pizza_description(size, pepperoni, cheese):
    if size == "S":
        size = "Small"
    if size == "M":
        size = "Medium"
    if size == "L":
        size = "Large"
    desc = f"Price for {size} pizza " # Initial description based on the ordered size of pizza
    if pepperoni == "Y":
        desc += "with Extra Pepperoni " # if user ordered an extra pepperoni a description will be concatenated to the original description
    if cheese == "Y":
        desc += "and with Extra Cheese" #if user ordered an extra cheese a description will also be concatenated to the latest description

    return desc # the function returns the description of the order


def pizza_order(): #Capture users pizza order
    while True:
        print("\nWelcome to my Pizza Order Calculator") # Short description of the program
        size = input("\nWhat size of pizza do you want? S, M, L : ").upper() # Capture the pizza size that the customer want to buy

        #checks if users input is valid based on the given choices
        if size not in ["S", "M", "L"]:
            print("Invalid size. Please choose S, M, or  L: ")
            continue # Will go back to Welcome message

        pepperoni = input("Do you want pepperoni on your pizza? Y or N: ").upper() # ask if user wants an extra pepperoni
        if pepperoni not in ["Y", "N"]:
            print("Invalid answer. Type Y or N: ")
            continue

        cheese = input("Do you want extra cheese? Y or N: ").upper() # ask if user wants an extra cheese
        if cheese not in ["Y", "N"]:
            print(" Invalid answer. Type Y or N: ")
            continue

        total = compute_order(size, pepperoni, cheese) # Based on the users selection, computes the total price by calling compute_order() function
       # print(total)
        description = pizza_description(size, pepperoni, cheese) #Determine the full description of the order
        #print(description)
        print(f"\n {description} is ${total}") # Display the order description and total price of the order

        another = input("Would you like to order another pizza?: ").upper() # asks user if user want to order another pizza
        if another != "Y":
            break

pizza_order()


