from art import logo, card_template
import random

cards_dict = {
    'A': 11,
    'K': 10,
    'Q': 10,
    'J': 10,
    '10': 10,
    '9': 9,
    '8': 8,
    '7': 7,
    '6': 6,
    '5': 5,
    '4': 4,
    '3': 3,
    '2': 2
}

def draw_a_card():
    return random.choice(list(cards_dict.keys()))

class Card:
    card_name = ""
    card_value = 0
    visible = False

    def  __init__(self, card_name, card_value, visible):
        self.card_name = card_name
        self.card_value = card_value
        self.visible = visible