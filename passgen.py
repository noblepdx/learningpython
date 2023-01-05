#password generator 

import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("welcome to noble's password generator")
num_letters= int(input("how many letters?\n")) 
num_symbols = int(input(f"how many symbols?\n"))
num_numbers = int(input(f"how many numbers?\n"))

pass_list = []

for z in range(1, num_letters + 1):
    pass_list += random.choice(letters)
for z in range(1, num_symbols + 1):
    pass_list += random.choice(symbols)
for z in range(1, num_numbers + 1):
    pass_list += random.choice(numbers)

random.shuffle(pass_list)

password = ""
for z in pass_list:
    password += z
print(password)

