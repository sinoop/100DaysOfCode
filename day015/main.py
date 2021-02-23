from cofee_machine import CoffeeMachine
from resources import MENU


def represents_int(s):
    try:
        int(s)
        return True
    except ValueError:
        return False


coffe_machine_instance = CoffeeMachine()
valid_item = []

valid_items = list(MENU.keys())

while True:
    print("==== Today's Menu ==== ")
    for i in range(0, len(valid_items)):
        print(f"{i + 1}.{valid_items[i]} (${MENU.get(valid_items[i]).get('cost')})")
    choice = input(f"What would you like ? :")
    if choice in valid_items or (represents_int(choice) and int(choice) in range(1, len(valid_items) + 1)):
        if represents_int(choice):
            item = valid_items[int(choice) - 1]
        else:
            item = choice

        if coffe_machine_instance.check_if_sufficient_ingredients_present(item):
            coffe_machine_instance.make_item(item)
    elif choice == 'report' or (represents_int(choice) and int(choice) == -1):
        coffe_machine_instance.print_ingredients_report()
        coffe_machine_instance.print_cash_balance_report()
    else:
        print("Invalid Selection")
