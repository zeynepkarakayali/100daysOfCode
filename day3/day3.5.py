"""
You are going to write a program that tests the compatibility between two people.
To work out the love score between two people:
Take both people's names and check for the number of times the letters in the word TRUE occurs. 
Then check for the number of times the letters in the word LOVE occurs. 
Then combine these numbers to make a 2 digit number.

For Love Scores less than 10 or greater than 90, the message should be:
"Your score is **x**, you go together like coke and mentos."

For Love Scores between 40 and 50, the message should be:
"Your score is **y**, you are alright together."

Otherwise, the message will just be their score. e.g.:
"Your score is **z**."
"""

# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
wholeString = name1 + name2
lowerString = wholeString.lower()

t = lowerString.count("t")
r = lowerString.count("r")
u = lowerString.count("u")
e = lowerString.count("e")
l = lowerString.count("l")
o = lowerString.count("o")
v = lowerString.count("v")
e = lowerString.count("e")

total1 = str(t + r + u + e)
total2 = str(l + o + v + e)
score = int(total1 + total2)

if((score < 10) or (score > 90)):
    print(f"Your score is {score}, you go together like coke and mentos.")
elif((score > 40) and (score < 50)):
    print(f"Your score is {score}, you are alright together.")
else:
    print(f"Your score is {score}.")