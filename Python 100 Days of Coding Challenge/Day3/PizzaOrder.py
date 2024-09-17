# 🚨 Don't change the code below 👇
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ").upper()
add_pepperoni = input("Do you want pepperoni? Y or N ").upper()
extra_cheese = input("Do you want extra cheese? Y or N ").upper()
# 🚨 Don't change the code above 👆
print(size)
print(add_pepperoni)
print(extra_cheese)

# Write your code below this line 👇
b = 0

if size == "S":
    b = 15
elif size == "M":
    b = 20
elif size == "L":
    b = 25
    if add_pepperoni == "Y":
        b += 2
    if extra_cheese == "Y":
        b += 1

print(f"Your size selected was {size}, your final bill is ${b}")