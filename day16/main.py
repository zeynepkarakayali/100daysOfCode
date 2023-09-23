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