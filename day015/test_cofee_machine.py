from unittest import TestCase
from cofee_machine import CoffeeMachine


class TestCoffeeMachine(TestCase):

    def setUp(self) -> None:
        self.coffee_machine = CoffeeMachine()

    def test_calculate_balance_coins(self):
        self.assertEqual(calculate_balance_coins(10))
        self.fail()
