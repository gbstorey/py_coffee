from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
from prettytable import PrettyTable
import os


def clear():
    print("\n" * 120)


menu = Menu()
coffeemaker = CoffeeMaker()
moneymachine = MoneyMachine()
can_make = ""
vending = True


def refill():
    water = 300
    milk = 200
    coffee = 100


while vending:
    print("Welcome to Python Coffee! What can I make for you?\n(admin: 'maintenance')")
    print(menu.get_items())
    order_name = input("Order: ")
    if order_name == "maintenance":
        task = input("What task would you like to perform? (refill/shutoff/report) ")
        if task == "refill":
            refill()
            coffeemaker.report()
        elif task == "shutoff":
            print("Shutting down...")
            vending = False
        elif task == "report":
            coffeemaker.report()
            moneymachine.report()
    else:
        drink = menu.find_drink(order_name)
        print(f"This drink costs ${drink.cost}.")
        if coffeemaker.is_resource_sufficient(drink) and moneymachine.make_payment(drink.cost):
            coffeemaker.make_coffee(drink)