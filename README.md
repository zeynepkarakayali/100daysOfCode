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

--------
### Day 10. 
### Project Name: Calculator
<br>
The goal of day 10 is to write a Calculator in code.
This calculator can do basic math operations like:

- addition
- subtraction
- multiplication
- division

The code of Day 10:
~~~
from art import logo

# ADD
def add(n1, n2):
    return n1 + n2

# SUBTRACT
def subtract(n1, n2):
    return n1 - n2

# MULTIPLY
def multiply(n1, n2):
    return n1 * n2

#DIVIDE
def divide(n1, n2):
    return n1 / n2

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}

print("Hello, Welcome to the calculator! ")
print("The operations you can execute with the calculator are: ")
for i in operations:
    print(i)

def calculator():
    print(logo)
    num1 = float(input("What's the first number? : "))

    operationFinished = False
    while not operationFinished:

        choice = input("Pick an operation: ")
        func = operations[choice]

        num2 = float(input("What's the second number? : "))

        result = func(num1, num2)
        print(f"{num1} {choice} {num2} = {result}")

        continuation = input(f"Type 'y' to continue calculating with {result} ,type 'n' to start a new calculation, or type 'e' to exit. ").lower()
        if(continuation == "y"):
            operationFinished = False
            num1 = result
        elif(continuation == "n"):
            operationFinished = True
            calculator()
        elif(continuation == "e"):
            operationFinished = True

calculator()
~~~
![Output of Day 10](https://github.com/zeynepkarakayali/100daysOfCode/blob/main/outputs/day10.png)

--------
### Day 11. 
### Project Name: The Blackjack Capstone Project
<br>
The goal of day 11 is to write the Blackjack game in code.

The rules of the game are:
- The deck is unlimited in size. 
- There are no jokers. 
- The Jack/Queen/King all count as 10.
- The the Ace can count as 11 or 1.
- Use the following list as the deck of cards:
- cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
- The cards in the list have equal probability of being drawn.
- Cards are not removed from the deck as they are drawn.
- The computer is the dealer.

The code of Day 11:
~~~
from art import logo
import random

def dealCard():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    cardChoice = random.choice(cards)
    return cardChoice

def sumCards(deck):
    if (sum(deck) == 21) and (len(deck) == 2):
        return 0
    
    if 11 in deck and sum(deck) > 21:
        deck.remove(11)
        deck.append(1)
        
    return sum(deck)


print("Welcome to the Blackjack Game! ")

def blackjack():

    game = input("Do you want to play the blackjack game? Type 'y' or 'n': ").lower()
    print(logo)

    myCards = []
    compCards = []
    gameFinished = False

    if(game == "y"):
        for i in range(2):
            myCards.append(dealCard())
            compCards.append(dealCard())

    elif(game == "n"):
        gameFinished = True

    while not gameFinished:
        myScore = sumCards(myCards)
        compScore = sumCards(compCards)
        print(f"   Your cards: {myCards}, current score: {myScore}")
        print(f"   Computer's first card: {compCards[0]}")

        game = input("Type 'y' to get another card, type 'n' to pass: ")
        if(game == "y"):
            myCards.append(dealCard())
            myScore = sumCards(myCards)
            if(myScore > 21):
                print("You went over! You lost! ")
                gameFinished = True
                break
        else:
            gameFinished = True

    while compScore != 0 and compScore < 17:
        compCards.append(dealCard())
        compScore = sumCards(compCards)

    print(f"Your final hand: {myCards}, final score: {myScore}")
    print(f"Computer's final hand: {compCards}, final score: {compScore}")
    if(myScore > 21):
        print("You went over. You lost the game! ")
    elif(compScore > 21):
        print("Computer went over. You win! ")
    elif(compScore == myScore):
        print("It's a draw!")
    elif(myScore == 21):
        print("You won with a Blackjack! ")
    elif(compScore == 21):
        print("Computer won with a blackjack! ")
    elif(myScore > compScore):
        print("You win! ")
    else:
        print("You lose! ")

blackjack()
~~~
![Output of Day 11](https://github.com/zeynepkarakayali/100daysOfCode/blob/main/outputs/day11.png)

--------
### Day 12. 
### Project Name: Number Guessing Game
<br>
The goal of day 12 is to write a Number Guessing game in code.

The game lets you choose difficulty. 

- In easy mode you have **10 attempts** to successfully guess the number 
- In hard mode you have **5 attempts** to successfully guess the number

The code of Day 12:
~~~
# NUMBER GUESSING GAME
import random

print("Welcome to the number guessing game! ")
print("I am going to think of a number between 1 and 100. Try to guess it! ")
difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()

attempt = 10
if(difficulty == 'hard'):
    attempt = 5

number = random.randint(0,100)
print(f"pstt, the number is: {number}. Act like you don't know it. ")

guess = 101
while (attempt > 0) and (guess != number):
    print(f"You have {attempt} attempts remaining to guess the number. ")
    guess = int(input("Make a guess: "))
    if(guess > number):
        print("Too high.")
        print("Guess again.")
    elif(guess < number):
        print("Too low.")
        print("Guess again.")
    else:
        print("Congrats! You have found the number.")
        print("Are you a magician :d")
    attempt -= 1

if(attempt == 0) and (guess != number):
    print("You ran out of attempts. :(")
~~~
![Output of Day 12](https://github.com/zeynepkarakayali/100daysOfCode/blob/main/outputs/day12.png)

--------
### Day 13. 
### Project Name: Debugging
<br>
The goal of day 13 is to debug old projects we did.

Note: I didn't include the outputs of the codes because I already included them before.

--------
### Day 14. 
### Project Name: Higher Lower Game
<br>
The goal of day 14 is to write:

[The Higher Lower Game](https://higherlowergame.com) in code.

The code of Day 14:

~~~
# The Higher Lower Game
import art
import gameData
import random


def higherLower():
    score = 0
    gameOver = False
    
    while not gameOver:

        print(art.logo)
        #print("\n")
        a = random.choice(gameData.data)
        b = random.choice(gameData.data)
        # print(a)
        # print(b)    

        while a == b:
            b = random.choice(gameData.data)
            print(b)

        print(f"Compare A: {a['name']}, a {a['description']}, from {a['country']}.")
        print(art.vs)
        print(f"Compare B: {b['name']}, a {b['description']}, from {b['country']}.")
        choice = input("\nWho has more followers? Type 'A' or 'B': ").lower()

        if(choice == "a"):     
            if(a["follower_count"] >= b["follower_count"]):
                score += 1
                print(f"You are right! Current score: {score}")
            else:
                print(f"Sorry that's wrong. Current score: {score}")
                gameOver = True

        elif(choice == "b"):     
            if(b["follower_count"] >= a["follower_count"]):
                score += 1
                print(f"You are right! Current score: {score}")
            else:
                print(f"Sorry that's wrong. Current score: {score}")
                gameOver = True 
        else:
            print(f"Sorry you typed wrong. Current score: {score}")
            gameOver = True

higherLower()
~~~
![Output of Day 14](https://github.com/zeynepkarakayali/100daysOfCode/blob/main/outputs/day14.png)

--------
### Day 15. 
### Project Name: Coffee Machine
<br>
The goal of day 15 is to write a Coffee Machine code:

The code of Day 15:

~~~
# ☕ MACHINE
import main

isOver = False
profit = 0

# TODO: 4. Check resources sufficient?
def checkResources(orderIngredients):
    """ Returns True when order can be made, False if ingredients are sufficent. """
    for item in orderIngredients:
        if main.resources[item] < orderIngredients[item]:
            print(f"Sorry there is not enough {item}.")
            return False
    return True

# TODO: 5. Process coins.
def sumMoney():
    print("Please insert coins.")
    quarters = int(input("how many quarters?: "))
    dimes = int(input("how many dimes?: "))
    nickels = int(input("how many nickels?: "))
    pennies = int(input("how many pennies?: "))

    return float((pennies * 0.01) + (nickels * 0.05) + (dimes * 0.1) + (quarters * 0.25))

# TODO: 6. Check transaction successful?
def transactionSuccessful(sum, cost):
    if sum >= cost:
        print(f"Here is ${round(sum - cost, 4)} in change.")
        global profit
        profit += cost
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False


# TODO: 7. Make Coffee.
def makeCoffee(coffee, orderIngredients):
    for item in orderIngredients:
        #print(item)
        #print(orderIngredients[item])
        main.resources[item] -= orderIngredients[item]
    print(f"Here is your {coffee}☕. Enjoy!")

while not isOver:
    # TODO: 1. Prompt user by asking “What would you like? (espresso/latte/cappuccino):”
    user = input("What would you like? (espresso/latte/cappuccino): ").lower()

    # TODO: 2. Turn off the Coffee Machine by entering “off” to the prompt.
    if user == "off":
        isOver = True

    # TODO: 3. Print report.
    elif user == "report":
        print(f"Water: {main.resources['water']}ml")
        print(f"Milk: {main.resources['milk']}ml")
        print(f"Coffee: {main.resources['coffee']}g")
        print(f"Money: ${profit}")

    else:
        userCoffee = main.MENU[user]
        #sumMoney()
        if checkResources(userCoffee["ingredients"]):
            sum = sumMoney()
            cost = userCoffee['cost']
            if transactionSuccessful(sum, cost):
                #print(profit)
                makeCoffee(user, userCoffee["ingredients"])
~~~
![Output of Day 15](https://github.com/zeynepkarakayali/100daysOfCode/blob/main/outputs/day15.png)

--------
### Day 16. 
### Project Name: Coffee Machine 2.0
<br>
The goal of day 16 is to write a Coffee Machine code with classes and objects:

The code of Day 16:

~~~
from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
moneyMachine = MoneyMachine()
coffeeMaker = CoffeeMaker()
isOver = False

while not isOver:

    choice = input(f"What would you like? {menu.get_items()}: ").lower()

    if choice == "off":
        isOver = True

    elif choice == "report":
        coffeeMaker.report()
        moneyMachine.report()
    else:
        drink = menu.find_drink(choice)
        if(drink != None):
            #print("Please insert coins. ")
            if coffeeMaker.is_resource_sufficient(drink) and moneyMachine.make_payment(drink.cost):
                coffeeMaker.make_coffee(drink)
~~~
![Output of Day 16](https://github.com/zeynepkarakayali/100daysOfCode/blob/main/outputs/day16.png)

--------
### Day 17. 
### Project Name: Quiz Game
<br>
The goal of day 17 is to write a Quiz Game by using:

[Open Trivia Database](https://opentdb.com/api_config.php) site.

The code of Day 17:

~~~
from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []

for item in question_data:
    new_question = Question(item["question"], item["correct_answer"])
    question_bank.append(new_question)

#print(question_bank[0].question)

quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()

print("You've completed the quiz. ")
print(f"Your final score was: {quiz.score}/{quiz.question_number}. ")
~~~
![Output of Day 17](https://github.com/zeynepkarakayali/100daysOfCode/blob/main/outputs/day17.png)
