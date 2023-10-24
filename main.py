from databasa import MENU
from databasa import resources
from math import *

order = input("What would you like? (espresso/latte/cappuccino): ")


def checking_resources(coffe_name):
    necessary_ingredients = MENU[coffe_name]["ingredients"]
    remainig_water = resources["water"]
    remaining_milk = resources["milk"]
    remaining_coffee = resources["coffee"]

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
        return f"Here is ${change} change."
    else:
        return "Sorry that's not enough money. Money refunded."



your_money = getting_coins()

money_procces = checking_price(your_money, order)
print(your_money)
print(money_procces)