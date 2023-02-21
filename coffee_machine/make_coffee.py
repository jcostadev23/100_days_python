from machine import MENU


def make_coffee(type_of_coffee, remaining_resources):
    water = remaining_resources["water"] - MENU[type_of_coffee]["ingredients"]["water"]
    remaining_resources["water"] = water
    if "milk" in MENU[type_of_coffee]["ingredients"]:
        milk = remaining_resources["milk"] - MENU[type_of_coffee]["ingredients"]["milk"]
        remaining_resources["milk"] = milk
    coffee = remaining_resources["coffee"] - MENU[type_of_coffee]["ingredients"]["coffee"]
    remaining_resources["coffee"] = coffee
    print("There is your coffee Enjoy! ☕️")
