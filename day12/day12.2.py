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