# Write your code below this line 👇
# Hint: Remember to import the random module first. 🎲
import random

value = random.randint(0,1)
#print(value)

if value == 1:
  result = 'Heads'
elif value == 0:
  result = 'Tails'

print(result)