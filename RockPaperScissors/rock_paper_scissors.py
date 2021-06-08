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

options = [rock, paper, scissors]

player = int(input("What do you choose?\nType 0 for Rock, 1 for Paper and 2 for Scissors: "))
computer = random.randint(0, 2)

print(f"\nYou chose:\n{options[player]}\n\nComputer chose:\n{options[computer]}")

if player == computer:
  print("Its a draw")
elif player == 0:
  if computer == 2:
    print("You win")
  else:
    print("You lose")
elif player == 1:
  if computer == 0:
    print("You win")
  else:
    print("You lose")
elif player == 2:
  if computer == 1:
    print("You win")
  else:
    print("You lose")