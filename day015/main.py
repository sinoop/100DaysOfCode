from cofee_machine import CoffeeMachine
from resources import MENU

c = CoffeeMachine()
valid_item = []

valid_items = MENU.keys()

while True:
    item_selected = input(f"What would you like? ({valid_items})? ")
    if item_selected in valid_items:
        if c.check_if_sufficient_ingredients_present(item_selected):
            c.make_item(item_selected)
    elif item_selected == 'report':
        c.print_report()
