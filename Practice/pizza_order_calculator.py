while True:
    print("\nWelcome to my Pizza Order Calculator")
    size = input("\nWhat size of pizza do you want? S, M, L : ").title()
    print(size)
    pepperoni = input("Do you want pepperoni on your pizza? Y or N: ").title()
    print(pepperoni)
    cheese = input("Do you want extra cheese? Y or N: ").title()


    if size == "L":
        large_price = 25
        if pepperoni == "Y":
            lextra_pep = 3
            if cheese == "Y":
                lextra_cheese = 1
                lpc_price = large_price + lextra_pep + lextra_cheese
                print(f"Price for L pizaa with extra Pepperoni and cheese is {lpc_price}")
            elif cheese == "N":
                nextra_cheese = 0
                lp_price = large_price + lextra_pep + nextra_cheese
                print(f"Price for L pizaa with extra Pepperoni with NO cheese is {lp_price}")

        elif pepperoni == "N":
            extra_pep = 0
            if cheese == "Y":
                extra_cheese = 1
                lc_price = large_price + extra_cheese
                print(f"Price for L pizaa with cheese but NO extra Pepperoni is {lc_price}")
            elif cheese == "N":
                extra_cheese = 0
                l_price = large_price
                print(f"Price for L pizaa with NO cheese and NO extra Pepperoni is {l_price}")


    elif size == "M":
        medium_price = 20
        if pepperoni == "Y":
            mextra_pep = 3
            if cheese == "Y":
                mextra_cheese = 1
                mpc_price = medium_price + mextra_pep + mextra_cheese
                print(f"Price for M pizaa with extra Pepperoni and extra Cheese is {mpc_price}")

            elif cheese == "N":
                extra_cheese = 0
                mpnc_price = medium_price + extra_cheese
                print(f"Price for M pizaa with extra Pepperoni but NO extra Cheese is {mpnc_price}")

        elif pepperoni == "N":
            mextra_pep = 0
            if cheese == "Y":
                mextra_cheese = 1
                mpc_price = medium_price + mextra_pep + mextra_cheese
                print(f"Price for M pizaa with NO extra Pepperoni and NO extra Cheese is {mpc_price}")

            elif cheese == "N":
                extra_cheese = 0
                mpnc_price = medium_price + extra_cheese
                print(f"Price for M pizaa with NO extra Pepperoni and  NO extra Cheese is {mpnc_price}")

    elif size == "S":
        small_price = 15
        if pepperoni == "Y":
            s_extra_pep = 2
            if cheese == "Y":
                s_extra_cheese = 1
                spc_price = small_price + s_extra_pep + s_extra_cheese
                print(f"Price for M pizaa with extra Pepperoni and extra Cheese is {spc_price}")
            elif cheese == "N":
                s_extra_cheese = 0
                spnc_price = small_price + s_extra_pep + s_extra_cheese
                print(f"Price for M pizaa with extra Pepperoni and extra Cheese is {spnc_price}")
        elif pepperoni == "N":
            s_extra_pep = 0
            if cheese == "Y":
                s_extra_cheese = 1
                snpc_price = small_price + s_extra_pep + s_extra_cheese
                print(f"Price for M pizaa with NO extra Pepperoni but with extra Cheese is {snpc_price}")
            elif cheese == "N":
                s_extra_cheese = 0
                spc_price = small_price + s_extra_pep + s_extra_cheese
                print(f"Price for M pizza with NO extra Pepperoni but with extra Cheese is {spc_price}")
