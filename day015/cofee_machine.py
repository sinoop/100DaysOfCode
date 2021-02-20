from operator import mod
from decimal import Decimal
from resources import resources, MENU

QUARTER_VALUE = Decimal("0.25")
DIME_VALUE = Decimal("0.10")
NICKEL_VALUE = Decimal("0.05")
PENNY_VALUE = Decimal("0.01")


def calculate_balance_coins(amount):
    """

    >>> calculate_balance_coins(0.25)
    (1, 0, 0, 0)

    >>> calculate_balance_coins(1.25)
    (5, 0, 0, 0)

    >>> calculate_balance_coins(1.26)
    (5, 0, 0, 1)

    >>> calculate_balance_coins(1.31)
    (5, 0, 1, 1)

    >>> calculate_balance_coins(1.36)
    (5, 1, 0, 1)

    >>> calculate_balance_coins(1.46)
    (5, 2, 0, 1)
    """
    quarters, balance = divmod(Decimal(str(amount)), QUARTER_VALUE)
    dimes, balance = divmod(balance, DIME_VALUE)
    nickels, balance = divmod(balance, NICKEL_VALUE)
    pennies, balance = divmod(balance, PENNY_VALUE)
    return int(quarters), int(dimes), int(nickels), int(pennies)
    # print(f"balance = {balance} quarters = {quarters}")


def check_and_give_balance(amount, total_given):
    """
    >>> check_and_give_balance(9.5,10)
    Total is $9.5, You have tendered $10. Balance amount is : $0.5
    True

    >>> check_and_give_balance(10,9.5)
    Total is $10, You have tendered $9.5. Insufficient coins. Please add $0.5 and try again. Dispencing the provided coins
    False
    """
    if amount == total_given:
        print("Exact amount tendered..!!")
        return True
    elif amount < total_given:
        balance = round(total_given - amount, 2)
        print(f"Total is ${amount}, "
              f"You have tendered ${total_given}. "
              f"Balance amount is : ${balance}")
        calculate_balance_coins(balance)
        return True
    else:
        balance = round(amount - total_given, 2)
        print(
            f"Total is ${amount}, You have tendered ${total_given}. "
            f"Insufficient coins. Please add ${balance} and try again. Dispencing the provided coins")
        return False


def get_coins() -> Decimal:
    print("Please insert coins")
    quarters = int(input("how many quarters : "))
    dimes = int(input("how many dimes : "))
    nickels = int(input("how many nickels : "))
    pennies = int(input("how many pennies : "))
    print(f"quarters = {quarters} dimes = {dimes} nickels= {nickels} pennies = {pennies}")

    return Decimal(str(quarters * QUARTER_VALUE + dimes * DIME_VALUE + nickels * NICKEL_VALUE + pennies * PENNY_VALUE))


class CoffeeMachine:
    ingredients = {}
    menu = {}

    def __init__(self):
        for i in resources:
            self.ingredients[i] = resources.get(i)
        for i in MENU:
            self.menu[i] = MENU[i]

    def check_if_sufficient_ingredients_present(self, item):
        for ingredient in self.menu.get(item).get('ingredients'):
            required_qty = self.menu.get(item).get('ingredients').get(ingredient)
            available_qty = self.ingredients[ingredient]
            if available_qty < required_qty:
                print(
                    f"insufficient {ingredient} to make the {item}. "
                    f"Need {required_qty - available_qty} more of {ingredient}")
                return False
        return True

    def make_item(self, item):
        cost = Decimal(self.menu.get(item).get('cost'))
        print(f"Cost is : ${cost}")

        if check_and_give_balance(cost, get_coins()):
            for ingredient in MENU.get(item).get('ingredients'):
                self.ingredients[ingredient] -= MENU.get(item).get('ingredients').get(ingredient)
                print(f"{ingredient} = {self.ingredients[ingredient]}")


if __name__ == "__main__":
    import doctest

    doctest.testmod()
