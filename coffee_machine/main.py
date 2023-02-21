
from calculate_money import calculate_money, calculate_till
from get_coffe_price import get_coffe_price
from has_enough_money import has_enough_money
from has_enough_resources import has_enough_resources
from machine import resources, money_on_till, MENU
from make_coffee import make_coffee

remaining_resources = resources.copy()

more_coffee = True

while more_coffee:
    client_choice = input("What would you like ? (espresso/ latte/ cappuccino: ").lower()

    if client_choice == "cappuccino" or client_choice == "latte" or client_choice == "espresso":
        print(get_coffe_price(client_choice))
    else:
        print("You need to chose one off the options")
        continue

    if not has_enough_resources(client_choice, remaining_resources):
        continue

    print("Please insert coins.")

    client_quarters = float(input("How many quarters? "))
    client_dimes = float(input("How many dimes? "))
    client_nickles = float(input("How many nickles? "))
    client_pennies = float(input("How many pennies? "))
    print(f"You insert: {calculate_money(client_quarters, client_dimes, client_nickles, client_pennies)}")

    if not has_enough_money(client_quarters, client_dimes, client_nickles, client_pennies, client_choice):
        continue

    make_coffee(client_choice, remaining_resources)
    print(f"You have on till: {calculate_till(money_on_till)} ")


