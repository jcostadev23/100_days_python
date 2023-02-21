from machine import resources

from machine import MENU


def has_enough_resources(coffee, remaining_resources):
    """verificar primeiro a ver se tem tudo primeiro """
    if remaining_resources["water"] <= MENU[coffee]["ingredients"]["water"]:
        print("Sorry not enough water")
        if input("Do you want to refuel the resources? 'yes' or 'no' ") == 'yes':
            remaining_resources["water"] = resources["water"]
        else:
            return False

    if remaining_resources["coffee"] <= MENU[coffee]["ingredients"]["coffee"]:
        print("Sorry not enough coffee.")
        if input("Do you want to refuel the resources? 'yes' or 'no' ") == 'yes':
            remaining_resources["coffee"] = resources["coffee"]
        else:
            return False

    if "milk" in MENU[coffee]["ingredients"] and remaining_resources["milk"] <= \
            MENU[coffee]["ingredients"]["milk"]:
        print("Sorry not enough milk.")
        if input("Do you want to refuel the resources? 'yes' or 'no' ") == 'yes':
            remaining_resources["milk"] = resources["milk"]
        else:
            return False

    return True
