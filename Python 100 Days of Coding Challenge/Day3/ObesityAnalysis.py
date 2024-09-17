# 🚨 Don't change the code below 👇
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
bmi = weight / (height**2)
bmi = int(round(bmi, 0))

print(f"your BMI is: {bmi}, status:")

if bmi < 18.5:
  print('underweight')
elif bmi < 25:
  print('normal weight')
elif bmi < 30:
  print('overweight')
elif bmi < 35:
  print('obese')
else:
  print('clinically obese')
