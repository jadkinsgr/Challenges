import random

names_string = 'Angela, Ben, Jenny, Michael, Chloe'
names = names_string.split(", ") #create a list from a string
victim = random.randint(0, len(names)-1)
print(f"{names[victim]} is going to buy the meal today!")
