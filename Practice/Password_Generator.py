import random
import string


print("Welcome to my Password Generator ")

#letters =['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
#digits = ['1', '2','3','4','5','6','7','8','9','0']
#symbols = ['!','@','#','$','&',']',')','(','{','/','>','%']
letters = string.ascii_letters
digits = string.digits
symbols = string.punctuation

pass_char_len = int(input("How many letters you want in your password? "))
sym_char_num = int(input("How many symbols you want in your password? "))
digit_num = int(input("How many digits you want in your password? "))

#password = []
# How to generate a password randomly.
'''
i = 1
for i in range(pass_char_len):
    password.append(random.choice(letters))
    i += 1
#print(password)

i = 1
for i in range(digit_num):
    password.append(random.choice(digits))
    i += 1

#print(password)

i = 1
for i in range(sym_char_num):
    password.append(random.choice(symbols))
    i += 1
#print(password)
'''
password = ([random.choice(letters) for _ in range(pass_char_len)] +
           [random.choice(digits) for _ in range(digit_num)] +
           [random.choice(symbols) for _ in range(sym_char_num)])

print(password)
random.shuffle(password)

final_password = ' '.join(password)

print(f" Final suggested password:  {final_password} ")