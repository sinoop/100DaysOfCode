import random
from os import name, system
from time import sleep

from art import card_template, logo
from card import Card
from person import Person

choice = "y"


def clear():
    # for windows
    if name == 'nt':
        _ = system('cls')
        # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')


while choice == 'y':
    human = Person(name="Sinoop", type_of_user="human")
    dealer = Person(name="Eric", type_of_user="dealer")

    human.draw_a_card(visible=True)
    human.draw_a_card(visible=True)
    dealer.draw_a_card(visible=True)
    dealer.draw_a_card(visible=False)
    dealer_win_status = dealer.check_if_won()

    if dealer_win_status == 'WON':
        print("Dealer has blackjack. Dealer won")

    while True:
        clear()
        human.print_cards_deck()
        dealer.print_cards_deck(print_only_visible=True)
        human_win_status = human.check_if_won()
        if human_win_status == 'NA':
            draw_new_card = input(
                "Do you want to draw a new card? Type 'y' or 'n': ").lower()
            if draw_new_card == 'n':
                break
            else:
                human.draw_a_card(True)
        else:
            draw_new_card = '-'
            break

    if draw_new_card == 'n':
        dealer_win_status = dealer.check_if_won()
        while dealer_win_status == 'NA' and dealer.total_score < 17:
            dealer.draw_a_card(visible=True)
            clear()
            human.print_cards_deck()
            dealer.print_cards_deck()
            dealer_win_status = dealer.check_if_won()

    clear()
    # print(f"dealer_win_status = {dealer_win_status} human_win_status = {human_win_status}")

    if human_win_status == 'LOST':
        print(f"{human.name} lost. Total > 21")
    elif dealer_win_status == 'WON':
        print(f"Dealer won.")
    elif human_win_status == 'WON':
        print(f"{human.name} won.")
    elif dealer_win_status == 'LOST':
        print(
            f"Dealer {dealer.name} lost. Total > 21. Dealer score : {dealer.total_score}")
    elif dealer_win_status == 'NA' and human_win_status == 'NA':
        if human.total_score > dealer.total_score:
            print(f"{human.name} won.")
        else:
            print(f"Dealer won.")

    human.print_cards_deck()
    dealer.print_cards_deck()
    choice = input(
        "Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower()
