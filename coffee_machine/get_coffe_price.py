from machine import MENU


def get_coffe_price(coffee):
    coffe_price = MENU[coffee]['cost']
    return float(coffe_price)
    # if coffee == "cappuccino":
    #     return MENU["cappuccino"]["cost"]
    # elif coffee == "latte":
    #     return MENU["latte"]["cost"]
    # elif coffee == "espresso":
    #     return MENU["espresso"]["cost"]
    # elif coffee == "resources":
    #     return check_resources()