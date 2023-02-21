from coffee_machine.machine import money_on_till


def calculate_money(quarters, dimes, nickles, pennies):
    a = quarters * 0.25
    b = dimes * 0.10
    c = nickles * 0.05
    d = pennies * 0.01
    return a + b + c + d

def calculate_till(money):
    total_money = sum(money)
    return total_money
