from card import Card, draw_a_card, cards_dict
from art import logo, card_template

class Person:
    name = ""
    type_of_user = ""
    total_score = 0
    total_shown_score = 0
    card_deck = []

    def __init__(self, name, type_of_user):
        self.name = name
        self.type_of_user = type_of_user
        self.total_score = 0
        self.total_shown_score = 0
        self.card_deck = []

    def print_cards_deck(self, print_only_visible=False):
        print(f"{self.name} total score: {self.total_shown_score}  Cards : \n")
        for card in self.card_deck:
            if len(card.name) == 2:
                card_to_print = card_template.replace("##", card.name)
            else:
                card_to_print = card_template.replace("##", card.name + " ")
            if print_only_visible and card.visible == False:
                print("")
            else:
                print(card_to_print)

    def recalcualte_total_score(self):
        total = 0 
        for card in self.card_deck:
            total += card.value

        if total > 21:
            for card in self.card_deck:
                if card.name == 'A':
                    total += 1
                else:
                    total += card.value
        
        self.total_score = total

    def draw_a_card(self, visible):
        """
        Draws a random card from the map and returns both key and value as a tuple
        """
        random_card = draw_a_card()
        card = Card(random_card, cards_dict[random_card], visible)

        self.card_deck.append(card)
        self.total_score += card.value
        if card.visible:
            self.total_shown_score += card.value

    def draw_initial_cards(self):
        if self.type_of_user == "human":
            for _ in range(0, 2):
                self.draw_a_card(visible=True)
        else:
            self.draw_a_card(visible=True)
            self.draw_a_card(visible=False)

    def check_if_won(self):
        check_value = 0
        if self.total_score > 21:
            check_value = 1
        elif self.total_score == 21:
            check_value = 0
        else:
            check_value = -1
        return check_value
