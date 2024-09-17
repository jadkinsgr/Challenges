'''
This code is a Love Calculator that takes two names as input, combines them, and calculates a "love score" based on the occurrence of specific letters in the combined names. Here's a summary of what the code does:

Asks the user for their name (name1) and their partner's name (name2).
Combines both names into a single string (combinedNames).
Converts the combined names to lowercase for consistent comparison (lowerNames).
Counts the occurrences of specific letters ('t', 'r', 'u', 'e') in the combined names and calculates the sum of these counts (firstDigit).
Counts the occurrences of specific letters ('l', 'o', 'v', 'e') in the combined names and calculates the sum of these counts (secondDigit).
Concatenates firstDigit and secondDigit into a single string and converts it to an integer to obtain the total love score (total).
Prints out a message based on the total love score:
If the score is less than 10 or greater than 90, it suggests that the two people "go together like coke and mentos."
If the score is between 40 and 50, it suggests that they are "alright together."
Otherwise, it simply displays the love score.
'''

print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

combinedNames = name1 + name2
lowerNames = combinedNames.lower()

t = lowerNames.count("t")
r = lowerNames.count("r")
u = lowerNames.count("u")
e = lowerNames.count("e")

firstDigit = t+r+u+e

l = lowerNames.count("l")
o = lowerNames.count("o")
v = lowerNames.count("v")
e = lowerNames.count("e")

secondDigit = l+o+v+e

total = int(str(firstDigit) + str(secondDigit))

if total < 10 or total > 90:
  print(f"your score is {total}, you go together like coke and mentos.")
elif total > 40 and total < 50:
  print(f"Your score is {total}, you are alright together.")
else:
  print(f"Your score is {total}")
