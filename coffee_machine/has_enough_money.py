from calculate_money import calculate_money
from get_coffe_price import get_coffe_price
from machine import money_on_till, MENU


def has_enough_money(quarters, dimes, nickles, pennies, coffee ):
    money = calculate_money(quarters, dimes, nickles, pennies)
    coffee_price = get_coffe_price(coffee)

    if input("You want to leave a tip? 'yes' or 'no'? ") == "yes":
        print("You give 10% tip!")
        coffee_price = coffee_price * 0.10 + coffee_price

    if money < coffee_price:
        print(f"Not enough money {money}")
        return False
    money_on_till.append(coffee_price)
    your_change = money - coffee_price

    print(f"Your change is: " '{:.2f}'.format(your_change))
    return True
