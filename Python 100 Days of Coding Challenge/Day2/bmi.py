# 1st input: enter height in meters e.g: 1.65
print("What is your height?")
height = input()
# 2nd input: enter weight in kilograms e.g: 72
print("What is your weight in kilograms?")
weight = input()
# 🚨 Don't change the code above 👆

# Write your code below this line 👇
height = float(height)
weight = float(weight)

bmi = weight/(height**2)
print(f"Your BMI is {int(bmi)}.")