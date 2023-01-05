# rock, paper, scissors with ascii art. this was fun. it actually works

import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

user_input = input("0 for Rock, 1 for Paper, or 2 for Scissors.\n")  

user_choice = int(user_input)
choices = [rock, paper, scissors]
if user_choice >= 3 or user_choice < 0:
  print("you typed an invalid number; you lose")
else:
    print(choices[user_choice])

print("computer chose:")

computer_choice = random.randint(0, 2)
print(choices[computer_choice])

if user_choice == computer_choice:
  print("it is a draw. try again.")
elif user_choice == 0 and computer_choice == 1:
  print("you lose")
elif user_choice == 1 and computer_choice == 2:
  print("you lose")
elif user_choice == 2 and computer_choice == 0:
  print("you lose")
else:
  print("you win!")
  
