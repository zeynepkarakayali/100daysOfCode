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