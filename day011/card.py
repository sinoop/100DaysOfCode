from art import logo, card_template
import random

cards_dict = {
    'A': 1,
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