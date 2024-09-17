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
#options = [rock, paper, scissors]
print('Welcome to Rock, Paper, Scissors!')
choice = int(
    input('What do you choose? Type 0 for Rock, 1 for Paper, or 2 for scissors.\n'))

if choice == 0:
  print(rock)
elif choice == 1:
  print(paper)
else:
  print(scissors)

comp = random.randint(0, 2)
print('computer chose:')
if comp == 0:
  print(rock)
elif comp == 1:
  print(paper)
else:
  print(scissors)
print("\n")


if choice == 0 and comp == 2:
  print('Congrats you win!')
elif choice > comp:
  print('Congrats you win!')
elif comp > choice:
  print('Sorry you lose!')
else:
  print("Looks to me like its a draw this time!")
