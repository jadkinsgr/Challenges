print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

# limits
limit = 120
if height >= limit:
    print("You can ride the roller coaster!")
else:
    print("I'm sorry, but you are not tall enough to ride.")

age = int(input("What is your age in years? "))
if age < 12:
    atotal = 7
elif age > 18:
    atotal = 12
else:
    atotal = 7

photo = input("Do you want a photo? Please answer 'yes' or 'no': ")
if photo.lower() == "yes":
    ptotal = 3
else:
    ptotal = 0

print(f"Your total cost comes out to be ${atotal + ptotal}")
