age = input()
# 🚨 Don't change the code above 👆
# Write your code below this line 👇
weeksinyear = 52
totalweeks = 52*90
age = int(age)
ageInWeeks = weeksinyear * age
remmainingWeeks = totalweeks - ageInWeeks
print(f"You have {remmainingWeeks} weeks left.")