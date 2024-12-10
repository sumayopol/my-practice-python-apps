print("Welcome to my Tip Calculator")

bill_amt = float(input("What was the bill amount?: \n"))

tip = float(input("How much tip would you like to give? 12, 13, 15 Percent? \n "))

num_of_friends = int(input("How many person will split the bill? : \n"))

total_bill = bill_amt + (bill_amt * tip/100)

share_amt = float(total_bill / num_of_friends)

#print(f"Here is the amount each need to share: {share_amt}" )

print(" Here is the amount each has to share : " + str(share_amt))