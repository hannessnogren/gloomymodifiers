
from .gloomcards import GloomCards
import pandas as pd
import itertools as it


class GloomDeck:
    def __init__(self, deck, cards=None):
        self.deck = deck
        if cards is None:
            self.cards = GloomCards()
        else:
            self.cards = cards
        return

    def set_cards(self, cards):
        self.cards = cards
        return

    def card_count(self, card=None):
        if card is not None:
            return self.deck[card] or 0
        else:
            return sum(self.deck.values())

    def cards_left(self, drawchain, card=None):
        return self.card_count(card) - drawchain.card_count(card)

    # TODO probability to draw set of cards
    def probability(self, cards):
        return

    def get_all_combinations(self, draw_two=False):
        card_counts = []
        card_names = []
        terminals = []
        for key, value in self.deck.items():
            if value > 0 and self.cards.is_rolling(key):
                card_counts.append(range(value+1))
                card_names.append(key)
            elif value > 0:
                terminals.append(key)

        # TODO Add terminal cards
        card_counts.append(terminals)
        card_names.append("terminal")

        return pd.DataFrame(it.product(*card_counts), columns=card_names)
