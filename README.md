# 100daysOfCode
The repository where I publish my progress of the 100 Days of Code by Dr. Angela Yu.

--------
## In this Program I am going to publish the "end of the day project"s outputs

--------
### Day 1. 
### Project Name: Band Name Generator
<br>
The goal of day 1 is to write a Band Name Generator.

The code of Day 1:
~~~
print("Hello! Welcome to the Band Name Generator! ")

color = input("Please write your favorite color. ")
animal = input("The animal you want to be the most? ")
zodiac = input("What is your zodiac sign? ")

print("The name of your band is: " + zodiac + " " + color + " " + animal)
~~~

![Output of Day 1](https://github.com/zeynepkarakayali/100daysOfCode/blob/main/outputs/day1.png)

--------
### Day 2. 
### Project Name: Tip Calculator
<br>
The goal of day 2 is to write a Tip Calculator.

The code of Day 2:
~~~
bill = float(input("What is your bill? "))
people = int(input("How many people will split the bill? "))
percentage = int(input("What is your tip percentage? "))
tip = (100 + percentage) / 100

pay = round((bill/people) * tip, 2)
print(f"Each person should pay: {pay}")
~~~
![Output of Day 2](https://github.com/zeynepkarakayali/100daysOfCode/blob/main/outputs/day2.png)

