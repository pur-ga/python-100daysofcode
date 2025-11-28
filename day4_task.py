# this one was confusing and I hope it works

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
ascii_art = [rock, paper, scissors]

import random

player_choice = int(input("What are you choosing? Type 0 for Rock, 1 for Paper and 2 for Scissors.\n"))
if player_choice >= 0 and player_choice <= 2:
    print(ascii_art[player_choice])

computer_choice = random.randint(0, 2)
print(f"Computer chose:")
print(ascii_art[computer_choice])

if player_choice >= 3 or player_choice < 0:
    print("You typed an invalid number, so no winnin' for ya.")
elif player_choice == 0 and computer_choice == 2:
    print("You win!")
elif computer_choice == 0 and player_choice == 2:
    print("You lose!")
elif computer_choice > player_choice:
    print("You lose!")
elif player_choice > computer_choice:
    print("You win!")
elif computer_choice == player_choice:
    print("It's a draw!")