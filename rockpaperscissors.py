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

user_input = input("What do you choose? Type 0 for Rock, 1 for Paper, or 2 for Scissors.\n")  

user_choice = int(user_input)
choices = [rock, paper, scissors]
if user_choice >= 3 or user_choice < 0:
  print("You typed an invalid number; you lose!")
else:
    print(choices[user_choice])

print("Computer chose:")

computer_choice = random.randint(0, 2)
print(choices[computer_choice])

if user_choice == computer_choice:
  print("It is a draw. Try again.")
elif user_choice == 0 and computer_choice == 1:
  print("You lose")
elif user_choice == 1 and computer_choice == 2:
  print("You lose")
elif user_choice == 2 and computer_choice == 0:
  print("You lose")
else:
  print("You win!")
  
