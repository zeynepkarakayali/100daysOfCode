"""
Congratulations, you've got a job at Python Pizza. Your first job is to build an automatic pizza order program.

Based on a user's order, work out their final bill.

Small Pizza: $15
Medium Pizza: $20
Large Pizza: $25

Pepperoni for Small Pizza: +$2
Pepperoni for Medium or Large Pizza: +$3

Extra cheese for any size pizza: + $1
"""

# 🚨 Don't change the code below 👇
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
bill = 0

if((size == "s") or (size == "S")):
    bill = 15
elif((size == "m") or (size == "M")):
    bill = 20
elif((size == "l") or (size == "L")):
    bill = 25
else:
    print("Sorry the size you entered is not available.")

if((add_pepperoni == "y") or (add_pepperoni == "Y")):
    if(size == ("s" or "S")):
        bill += 2
    else:
        bill += 3
elif((add_pepperoni == "n") or (add_pepperoni == "N")):
    bill = bill
else:
    print("Sorry the choice you entered is not available.")


if((extra_cheese == "y") or (extra_cheese == "Y")):
    bill += 1;
elif((extra_cheese == "n") or (extra_cheese == "N")):
    bill = bill
else:
    print("Sorry the choice you entered is not available.")

print(f"Your final bill is: ${bill}.")