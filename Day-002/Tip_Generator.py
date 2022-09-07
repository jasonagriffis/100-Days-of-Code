# Simple tip generator
# Jason Griffis
# 09/04/2022

#If the bill was $150.00, split between 5 people, with 12% tip.

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇
bill = float(input("How much was the bill? "))
number_of_people = int(input("How many people were there? "))
tip_percentage = int(input("What percentage of a tip would you like to leave? (15, 20, 25) "))
total = 0
if tip_percentage == 15:
  total = (bill / number_of_people) * 1.15
elif tip_percentage == 20:
  total = (bill / number_of_people) * 1.20
elif tip_percentage == 25:
  total = (bill / number_of_people) * 1.25
else:
  print("Not a valid entry!")

print(f"The total for each person is {total:.2f}")