# TIP CALCULATOR PROJECT

#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇

bill = float(input("What is your bill? "))
people = int(input("How many people will split the bill? "))
percentage = int(input("What is your tip percentage? "))
tip = (100 + percentage) / 100

pay = round((bill/people) * tip, 2)
print(f"Each person should pay: {pay}")