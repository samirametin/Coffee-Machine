from databasa import MENU
from databasa import resources
from math import *


def checking_resources(coffe_ingredient):
    for item in coffe_ingredient:
        if resources[item] <= ingredients[item]:
            print(f"Sorry there is not enough {item}")
            return False
    return True


def getting_coins():
    print("Please insert coins.")
    quarters = int(input("How many quarters?: "))
    dimes = int(input("How many dimes?: "))
    nickels = int(input("How many nickles?: "))
    pennies = int(input("How many pennies?: "))
    total = round((quarters * 0.25 + dimes * 0.1 + nickels * 0.05 + pennies * 0.01), 2)
    return total


def checking_price(money, coffee_name):
    coffee_price = MENU[coffee_name]["cost"]
    if money >= coffee_price:
        change = round(money - coffee_price, 2)
        print(f"Here is ${change} change.")
        global budget
        budget += coffee_price
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False


def make_coffee(coffee_name, order_ingredients):
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {coffee_name}! Enjoy!")


budget = 0
is_on = True
while is_on:
    order = input("What would you like? (espresso/latte/cappuccino): ")
    if order == "off":
        is_on = False
    elif order == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}gr")
        print(f"Money: ${budget}")
    else:
        ingredients = MENU[order]["ingredients"]
        if checking_resources(ingredients):
            your_money = getting_coins()
            if checking_price(your_money, order):
                make_coffee(order, ingredients)

