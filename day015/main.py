from cofee_machine import CoffeeMachine

c = CoffeeMachine()
while True:
    item_selected = input("What would you like? (espresso/latte/cappuccino)? ")
    if item_selected == 'espresso' or item_selected == 'latte' or item_selected == 'cappuccino':
        if c.check_if_sufficient_ingredients_present(item_selected):
            c.make_item(item_selected)
