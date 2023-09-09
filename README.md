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

--------
### Day 3. 
### Project Name: Treasure Island Game
<br>
The goal of day 3 is to write a console Game called Treasure Island.

The code of Day 3:
~~~
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

#Write your code below this line 👇
print("You are walking in an echanted forest and come into a cross road.")
road = input("Which way are you going to choose? Left or Right? ").lower()

if(road == "right"):
    print("The eagles attacked you. Game Over.")
elif(road == "left"):
    print("You are lucky. You may pass.")

    print("Now you arrived at a dark grey pond.")
    swim = input('Are you going to "swim" or are you going to "wait?" ').lower()

    if(swim == "swim"):
        print("The piranhas attacked you. You died. Game Over.")
    else:
        print("A boat arrived! You crossed the lake unharmed.")
        door = input('You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which colour do you choose? ').lower()

        if(door == "yellow"):
            print("YOU WON THE GAME!!!")
        else:
            print("You lost try again. :(")

else:
    print("There are no roads like that.")
~~~
![Output of Day 3](https://github.com/zeynepkarakayali/100daysOfCode/blob/main/outputs/day3.png)

### Day 4. 
### Project Name: Rock Paper Scissors Game
<br>
The goal of day 4 is to write a game called Rock Paper Scissors.

The code of Day 4:
~~~
import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
print("Welcome to the rock paper scissors game!")
player = input("You need to make a choice. Rock, paper or scissors? ").lower()

options = [rock,paper,scissors]
len = len(options)

num = random.randint(0, len-1)
computer = options[num]

print(f"\nThe computer played: ")
print(computer)

# the player played rock
if(player == "rock"):
    print(f"You played: {rock}")
    #computer played rock
    if(computer == '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''):
        print("ITS'A DRAW!")
    # computer played paper
    elif(computer == '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''):
        print("The computer won :(")
    # computer played scissors
    elif(computer == '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''):
        print("YOU WON! CONGRATS!")

# player played paper
elif(player == "paper"):
    print(f"You played: {paper}")
    # computer played rock
    if(computer == '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''):
        print("YOU WON! CONGRATS!")
    # computer played paper
    elif(computer == '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''):
        print("ITS'A DRAW!")

    #computer played scissors
    elif(computer == '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''):
        print("The computer won :(")

# player played scissors
elif(player == "scissors"):
    print(f"You played: {scissors}")
    # computer played rock
    if(computer == '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''):
        print("The computer won :(")
    # computer played paper
    elif(computer == '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''):
        print("YOU WON! CONGRATS!")

    #computer played scissors
    elif(computer == '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''):
        print("ITS'A DRAW!")
~~~
![Output of Day 4](https://github.com/zeynepkarakayali/100daysOfCode/blob/main/outputs/day4.png)
