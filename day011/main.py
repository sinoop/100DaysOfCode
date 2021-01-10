import random
from os import name, system
from time import sleep

from art import card_template, logo
from card import Card, Person

choice = "y"
win_check = -1
human = Person(name="Sinoop", type="human")
dealer = Person(name="Eric", type="dealer")

def clear():
    # for windows
    if name == 'nt':
        _ = system('cls')
        # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')


while choice == 'y':
    Person.draw_a_card(human, True)
    Person.draw_a_card(human, True)
    human.print_cards_deck()
    Person.draw_a_card(dealer, True)
    Person.draw_a_card(dealer, False)
    dealer.print_cards_deck(print_only_visible=True)

    draw_new_card = input(
        "Do you want to draw a new card? Type 'y' or 'n': ").lower()
    while draw_new_card == 'y' and win_check < 0:
        Person.draw_a_card(human, True)
        sleep(1)
        clear()
        human.print_cards_deck()
        win_check = human.check_if_won()
        if win_check < 0:
            draw_new_card = input(
                "Do you want to draw a new card? Type 'y' or 'n': ").lower()
        elif win_check > 0:
            print(
                f"You have lost. Total > 21. Your score : {human.total_score}")
            draw_new_card = 'n'
            break
        else:
            print(f"You won.. Your score : {human.total_score}")
            draw_new_card = 'n'
            break

    if draw_new_card == 'n':
        win_check = dealer.check_if_won()
        if win_check < 0:
            continue
        elif win_check > 0:
            print(
                f"Dealer {dealer.name} lost. Total > 21. Dealer score : {dealer.total_score}")
            break
        else:
            print(f"Dealer won.. Dealer score : {dealer.total_score}")
            break
        Person.draw_a_card(dealer, True)
        while dealer.check_if_won() < 0:
            Person.draw_a_card(dealer, True)

    win_check = dealer.check_if_won()
    if win_check < 0:
        continue
    elif win_check > 0:
        print(
            f"Dealer {dealer.name} lost. Total > 21. Dealer score : {dealer.total_score}")
        break
    else:
        print(f"Dealer won.. Dealer score : {dealer.total_score}")
        break

    choice = input(
        "Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower()
