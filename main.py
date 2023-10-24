from databasa import MENU
from databasa import resources
from math import *


def checking_resources(coffe_name):
    ingredients = MENU[coffe_name]["ingredients"]
    for item in ingredients:
        if resources[item] < ingredients[item]:
            print(f"Sorry there is not enough {item}")
        else:
            resources[item] -= ingredients[item]



def getting_coins():
    print("Please insert coins.")
    quarters = int(input("How many quarters?: "))
    dimes = int(input("How many dimes?: "))
    nickels = int(input("How many nickles?: "))
    pennies = int(input("How many pennies?: "))
    total = quarters * 0.25 + dimes * 0.1 + nickels * 0.05 + pennies * 0.01
    return total


def checking_price(money,coffee_name):
    coffee_price = MENU[coffee_name]["cost"]
    if money >= coffee_price:
        change = round(money - coffee_price, 2)

        return f"Here is ${change} change.\nHere is your {coffee_name}! Enjoy!"
    else:
        return "Sorry that's not enough money. Money refunded."


budget = 0
def coffe_machine():
    order = input("What would you like? (espresso/latte/cappuccino): ")
    if order == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}gr")
        print(f"Money: ${budget}")
    checking_resources(order)
    your_money = getting_coins()

    money_procces = checking_price(your_money, order)
    print(your_money)
    print(money_procces)
