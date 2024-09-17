#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇
totalbill=float(input("What is the total Bill?"))
people=int(input("How many people are there?"))
tip_percentage=(float(input("% of the bill added as tip?")))/100

# print(totalbill)
# print(people)   
# print(tip_percentage)

totalPerPerson =  (totalbill/people) * (1+tip_percentage)
totalPerPerson = round(totalPerPerson, 2)

print(f"If the bill was {totalbill}, split between {people} people, with a {tip_percentage*100}% tip. Each person should pay ${totalPerPerson}.")