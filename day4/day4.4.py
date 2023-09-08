# ROCK PAPER SCISSORS GAME 
# Go to https://replit.com/@appbrewery/rock-paper-scissors-start?v=1
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