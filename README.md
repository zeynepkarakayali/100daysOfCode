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

--------
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

--------
### Day 5. 
### Project Name: Password Generator
<br>
The goal of day 5 is to write a Python Password Generator that consists numbers, letters and symbols.

The code of Day 5:
~~~
#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91

"""
password = ""
for i in range(0, nr_letters):
    password += random.choice(letters)

for i in range(0, nr_symbols):
    password += random.choice(symbols)

for i in range(0, nr_numbers):
    password += random.choice(numbers)
    
print(f"Your new password is: {password}")
"""

#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P
passwordList = []

for i in range(0, nr_letters):
    passwordList += random.choice(letters)

for i in range(0, nr_symbols):
    passwordList += random.choice(symbols)

for i in range(0, nr_numbers):
    passwordList += random.choice(numbers)

random.shuffle(passwordList)
#print(passwordList)

password = ""
for a in passwordList:
    password += a
print(password)
~~~
![Output of Day 5](https://github.com/zeynepkarakayali/100daysOfCode/blob/main/outputs/day5.png)

--------
### Day 6. 
### Project Name: Escaping the Maze
<br>
The goal of day 6 is to solve a challenge named Escaping the Maze.
In this day, we solved a bunch of coding challenges in 

[https://reeborg.ca/index_en.html]  and the last challenge was an escaping the maze coding challenge for our robot Reeborg.
<br> <br>

![Output of Day 6](https://github.com/zeynepkarakayali/100daysOfCode/blob/main/outputs/day6.png)

--------
### Day 7. 
### Project Name: Hangman Game
<br>
The goal of day 7 is to write the Hangman Game.
In this day, we split the game step by step and solve them one by one.

The code of Day 7:
~~~
#Step 5
# HANGMAN GAME

import hangman_art
import hangman_words
import random

chosen_word = random.choice(hangman_words.word_list)
word_length = len(chosen_word)

end_of_game = False
lives = 6

print(f"{hangman_art.logo}")
print(f'Pssst, the solution is {chosen_word}.')

display = []
for _ in range(word_length):
    display += "_"

while not end_of_game:
    guess = input("Guess a letter: ").lower()

    if guess in display:
        print("You already guessed this word. ")

    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter

    if guess not in chosen_word:
        print(f"The letter {guess} is not in the word. ")
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You lose.")

    print(f"{' '.join(display)}")

    if "_" not in display:
        end_of_game = True
        print("You win.")

    print(hangman_art.stages[lives])
~~~
![Output of Day 7](https://github.com/zeynepkarakayali/100daysOfCode/blob/main/outputs/day7.png)

--------
### Day 8. 
### Project Name: Caesar's Cipher
<br>
The goal of day 8 is to write a Caesar's Cipher code.
In this day, we split the cipher code step by step and solve them one by one.

The code of Day 8:
~~~
from art import logo

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(start_text, shift_amount, cipher_direction):
  end_text = ""
  if cipher_direction == "decode":
    shift_amount *= -1
  for char in start_text:
    if char in alphabet:
        position = alphabet.index(char)
        new_position = position + shift_amount
        end_text += alphabet[new_position]
    else:
        end_text += char
    
  print(f"Here's the {cipher_direction}d result: {end_text}")

print(logo)

user = True
while user:
    if user:
        direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
        text = input("Type your message:\n").lower()
        shift = int(input("Type the shift number:\n"))
        if(shift > 26):
           shift %= 26
        caesar(start_text=text, shift_amount=shift, cipher_direction=direction)
        var = input("Do you want to restart the program. Type 'yes' if you want to go again. Otherwise type 'no'. ").lower()
        if(var == "yes"):
           user = True
        elif(var == "no"):
           user = False
~~~
![Output of Day 8](https://github.com/zeynepkarakayali/100daysOfCode/blob/main/outputs/day8.png)

--------
### Day 9. 
### Project Name: Secret Auction
<br>
The goal of day 9 is to write a Secret Auction Program in code.

For this day the goal is normally to write a **secret** auction program that's why we should use the clear() function from replit but since I usually prefer to write my codes in [VsCode](https://code.visualstudio.com/) I didn't use the function. That's why my auction turned out to be *not so secret* auction.

The code of Day 9:
~~~
from art import logo

def auction(bidders):

    highestBid = 0
    highestBidder = ""

    for bidder in bidders:
        if(bidders[bidder] > highestBid):
            highestBid = bidders[bidder]
            highestBidder = bidder
    print(f"The winner of the auction is: {highestBidder} with a bid of ${highestBid}")

bidders = {}
biddingFinished = False
while not biddingFinished:
    print("Welcome to the secret auction program. ")
    name = input("What is your name? ")
    bid = int(input("What is your bid? "))
    continuee = input("Are there any other bidders? Type 'yes' or 'no'. ").lower()
    bidders[name] = bid

    if continuee == "no":
        auction(bidders)
        biddingFinished = True
    elif continuee == "yes":
        auction(bidders)
~~~
![Output of Day 9](https://github.com/zeynepkarakayali/100daysOfCode/blob/main/outputs/day9.png)
