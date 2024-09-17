#Write your code below this row 👇
# print(3%3)
# print(5%5)
# print(10%5)
# print(12%3)
# print(15%5)
# print(15%3)

for number in range(1, 101):
  if number % 3 == 0 and number % 5 == 0:
    print("Fizzbuzz'")
  elif number % 3 == 0:
    print("Fizz")
  elif number % 5 == 0:
    print("Buzz")
  else:
    print(number)
