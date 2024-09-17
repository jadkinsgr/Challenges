print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
age = int(input("What is your age in years? "))

# limits
limit = 120
if height >= limit:
    print("You can ride the roller coaster!")
    if age < 12:
        print("Please pay $7.")
    elif age > 18:
        print("Please pay $12.")
    else:
        print("Please pay $7.")
else:
    print("I'm sorry, but you are not tall enough to ride.")
