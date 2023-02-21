import coffee_maker
from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()
while True:
    choice = input(f"Qual a sua escolha? , {menu.get_items()}")
    if choice == "off":
        break
    elif choice == "report":
        money_machine.report()
        coffee_maker.report()
    my_coffee = menu.find_drink(choice)
    if my_coffee is not None:
        if coffee_maker.is_resource_sufficient(my_coffee):
            if money_machine.make_payment(my_coffee.cost):
                coffee_maker.make_coffee(my_coffee)
