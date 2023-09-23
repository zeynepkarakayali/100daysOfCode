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