target = int(1000) # Enter a number between 0 and 1000
# 🚨 Do not change the code above ☝️

# Write your code here 👇
total = 0
for number in range(1, 101):
    if number % 2 == 0: #just grabs the even numbers
        total += number
print(total)