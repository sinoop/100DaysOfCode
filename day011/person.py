from card import Card, draw_a_card, cards_dict
from art import logo, card_template


class Person:
    def __init__(self, name, type_of_user):
        self.name = name
        self.type_of_user = type_of_user
        self.total_score = 0
        self.total_shown_score = 0
        self.card_deck = []

    def print_cards_deck(self, print_only_visible=False):
        card_to_print = ""
        for card in self.card_deck:
            # if len(card.card_name) == 2:
            #     card_to_print = card_template.replace("##", card.card_name)
            # else:
            #     card_to_print = card_template.replace("##", card.card_name + " ")

            if print_only_visible and card.visible == False:
                card_to_print += " __"
                # print("")
            else:
                card_to_print += " " + card.card_name
                # print(card_to_print)
        if print_only_visible:
            print(
                f"{self.name} total score: {self.total_shown_score}  Cards : {card_to_print}")
        else:
            print(
                f"{self.name} total score: {self.total_score}  Cards : {card_to_print}")

    def recalcualte_total_score(self):
        total = 0
        total_visible = 0
        for card in self.card_deck:
            # print (f"card_name  = {card.card_name}")
            total += card.card_value
            if card.visible == True:
                total_visible += card.card_value

        if total > 21:
            total = 0
            total_visible = 0

            for card in self.card_deck:
                if card.card_name == 'A':
                    total += 1
                    if card.visible == True:
                        total_visible += 1
                else:
                    total += card.card_value
                    if card.visible == True:
                        total_visible += card.card_value

        self.total_score = total
        self.total_shown_score = total_visible
        # print(f"self.total_score = {self.total_score} self.total_shown_score = {self.total_shown_score}")

    def draw_a_card(self, visible):
        """
        Draws a random card from the map and returns both key and value as a tuple
        """
        random_card = draw_a_card()
        card = Card(random_card, cards_dict[random_card], visible)

        self.card_deck.append(card)
        self.recalcualte_total_score()

    def draw_initial_cards(self):
        if self.type_of_user == "human":
            for _ in range(0, 2):
                self.draw_a_card(visible=True)
        else:
            self.draw_a_card(visible=True)
            self.draw_a_card(visible=False)

    def check_if_won(self):
        if self.total_score > 21:
            check_value = 'LOST'
        elif self.total_score == 21:
            check_value = 'WON'
        else:
            check_value = 'NA'
        return check_value
