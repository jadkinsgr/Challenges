from Art import logo
import random

version = input("How would you like to play? Please type 'Easy' or 'Hard'")

if version == 'Hard':
    tryCount = 5
if version == 'hard':
    tryCount = 5
elif version == 'Easy':
    tryCount = 10
elif version == 'easy':
    tryCount = 10
else: 
    print('please type a valid version')


number = random.randrange(0,100)
#print(f"cheat code: the number is {number}")
print(f"You have selected the {version} version. You now have exactly {tryCount} trys to guess the correct number between 0 and 100. Good luck!")

tries = 0
while tries < tryCount:
    tries += 1
    triesRemaining = tryCount - tries
    guess = int(input("what is your guess? "))
    if tries == tryCount:
        print(f"Sorry, but you have ran out of tries. The number was {number}! Play again!")
    elif guess == number: 
        print(f"You got it! the number was {number}! Great job")
        break
    elif guess < number:
        print(
            f"Oooo sorry, the your guess was too low, the number is higher. You have {triesRemaining} tries left")
    elif guess > number:
        print(
            f"Oooo sorry, the your guess was too high, the number is lower. You have {triesRemaining} tries left")